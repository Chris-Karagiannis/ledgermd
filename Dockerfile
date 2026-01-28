FROM node:22.12 AS build-vue
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build


FROM python:3.13
WORKDIR /app/backend
COPY backend/ ./
RUN pip install --no-cache-dir -r requirements.txt

COPY --from=build-vue /app/frontend/dist /app/frontend/dist

EXPOSE 5000

CMD ["python", "app.py"]