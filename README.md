
# Real-Time Data Pipeline with Dockerized Services

## Overview

This project encapsulates a real-time data processing and visualization pipeline within a Docker ecosystem. The core functionality simulates a random walk data generation through a Python application. This data is then streamed into a Kafka cluster, consisting of 3 brokers for robust data handling and redundancy. Telegraf acts as a data collection and publishing agent that subscribes to Kafka topics and persists the data into InfluxDB, a time-series database optimized for high-write loads and real-time analytics. Finally, Grafana, a leading open-source platform for monitoring and visualization, reads the stored data from InfluxDB and presents it in a user-friendly dashboard format.

## Architecture

![Random Walk Simulation](architecture.png "Random Walk Data Pipeline's Architecture")
- **Python Application**: Dockerized service simulating random walk data generation, with the output being a stream of data points.
- **Kafka**: A high-throughput distributed messaging system that manages the data stream provided by the Python application. Implemented with 3 brokers to ensure data availability and fault tolerance.
- ** **: A UI interface to visualize what's happening inside Kafka.
- **Telegraf**: Ingests data from Kafka and writes to InfluxDB, ensuring that the data flow is seamless and efficient.
- **InfluxDB**: Stores the time-series data and provides capabilities for fast data retrieval, which is essential for real-time analytics.
- **Grafana**: Connects to InfluxDB and provides real-time visualization of the data, with capabilities for creating comprehensive dashboards, setting alerts, and exploring metrics.

## Workflow

1. The Dockerized Python application generates the data and publishes it to Kafka.
2. Kafka receives the data and ensures it's distributed appropriately across the brokers, maintaining the data's integrity and availability.
3. Telegraf, configured within the same Docker network, subscribes to Kafka topics, collects the data, and writes it into InfluxDB.
4. InfluxDB, running as a Docker service, stores the data with high write and read efficiency.
5. Grafana, also part of the Docker composition, reads the data from InfluxDB and provides a powerful interface for data visualization.

## Docker Composition

The project is orchestrated using Docker Compose, which manages the lifecycle of all the services involved. Each service is containerized, ensuring consistency across different environments and simplifying the setup and scaling processes. The `docker-compose.yml` file includes the configuration for each service, including environment variables, volume mappings, network settings, and dependencies.

## Getting Started

To deploy this project:

1. Clone the repository to your local machine.
2. Navigate to the directory containing the `docker-compose.yml` file.
3. Run `docker-compose up` to start all the services.
4. Once the services are up, access Grafana's web interface to visualize the data.

## Dependencies

- Docker and Docker Compose must be installed on the machine where the project is deployed.

## Contributing

Contributions to the project are welcome. Contributors can clone the repository, make their changes, and submit a pull request for review.

## Conclusion

This project demonstrates a complete end-to-end real-time data pipeline, showcasing the power of Dockerized applications for data generation, streaming, storage, and visualization. It provides a template for similar applications where real-time data processing is required.

For detailed instructions, please refer to the README.md file within the project repository.
