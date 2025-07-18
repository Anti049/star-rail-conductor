# Stage 1: Build the SvelteKit frontend
FROM node:20 AS builder

WORKDIR /app/frontend

COPY frontend/package.json frontend/package-lock.json ./

RUN npm install

COPY frontend/ ./

RUN npm run build

# Stage 2: Setup the Python environment and final image
FROM python:3.12-slim

WORKDIR /app

# Install supervisor
RUN apt-get update && apt-get install -y supervisor

# Copy Python dependencies for backend and bot
COPY backend/requirements.txt ./backend/
COPY discord-bot/requirements.txt ./discord-bot/
RUN pip install --no-cache-dir -r backend/requirements.txt
RUN pip install --no-cache-dir -r discord-bot/requirements.txt

# Copy the built frontend from the builder stage
COPY --from=builder /app/frontend/build ./frontend/build

# Copy the backend and bot source code
COPY backend/ ./backend/
COPY discord-bot/ ./discord-bot/

# Copy the supervisor configuration
COPY supervisor.conf /etc/supervisor/conf.d/app.conf

# Expose the port FastAPI will run on
EXPOSE 8000

# You will need to pass your Discord token as an environment variable
# Example: docker run -p 8000:8000 -e DISCORD_TOKEN="your_token_here" my-app
ENV DISCORD_TOKEN=""

# Start supervisor which in turn starts our services
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/app.conf"]