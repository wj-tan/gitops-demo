# Use official Nginx image
FROM nginx:alpine

# Remove the default static files
RUN rm -rf /usr/share/nginx/html/*

# Copy our static files to the Nginx web root
COPY index.html /usr/share/nginx/html/
COPY styles.css /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Use default CMD provided by nginx image
