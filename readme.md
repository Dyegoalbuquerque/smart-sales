# Smart Sales system

Sales API is a microservice designed for handling product and sales operations with clean architecture principles. It supports creation, listing, and cancellation of sales, applying tax rules, and follows best practices like DDD, CQRS, and RESTful design.

The project also includes a data engineering workflow using **Apache Airflow** to extract, transform, and load (ETL) large datasets of sales, demonstrating batch processing and orchestration capabilities.

### 📊 Data-Driven Foundation

This system is built with a **data-driven architecture**, designed to serve as a reliable source of structured sales data. It enables downstream integration with **AI and Analytics teams**, providing clean, consistent, and high-volume datasets that are essential for training models, generating insights, and supporting intelligent decision-making.

---

## 🧩 Key Concepts and Architecture

- .NET 8, C#, RESTful API
- Domain-Driven Design (DDD)
- CQRS with MediatR
- EF Core with PostgreSQL
- AutoMapper
- Automated test with XUnit C#
- Docker + Docker Compose
- Ocelot API Gateway
- Apache Airflow (ETL/ELT pipeline)
- Pytest for automated tests on the data pipeline
- Git Flow & Semantic Commits

---

## ⚙️ Configuration Project

This section includes links to the detailed documentation for configuration of the project:

## Database Configuration Documentation

This document provides guidelines on how to configure and apply database migrations for the project.

## Prerequisites

Before starting, ensure you have the following tools installed:

- **.NET SDK** (version 5 or higher)
- **Entity Framework Core CLI** (`dotnet ef`)
- Ensure your project is set up correctly with the necessary connection strings and `DbContext`.

## Folder Structure

This guide assumes the following project folder structure:

- `./SalesApi.Infrastructure` - This folder contains the Entity Framework Core migration files.
- `./src` - This folder contains the source code and the Web API project.

## Adding a Migration

To add a new migration for the database, run the following command from the `./SalesApi.Infrastructure` folder:

```bash
 dotnet ef migrations add SalesDbMigration --output-dir Migrations --context SalesDbContext
```

## Applying Migration

To applying migration for the database, run the following command from the `./src` folder:

```bash
 dotnet ef database update --project ./SalesApi.Infrastructure --startup-project ./SalesApi.Presentation
```



## Running the Project
Once you've set up the project and configured the database, you can run it locally.

Run the Application
To start the application, execute the following command from the root of the project:

```bash
dotnet run --project ./SalesApi.Presentation
```
or

```bash
docker-compose up --build
```

## Testing the Project
Unit Tests
To run unit tests for the project, navigate to the test project directory (if separate) and execute:

```bash
dotnet test 
```

## 📡 Endpoints

Overview of available API endpoints:

| HTTP Method | Path             | Description                                    |
|-------------|------------------|------------------------------------------------|
| `GET`       | `/products`      | List products.                                 |
| `POST`      | `/products`      | Create a new product.                          |
| `GET`       | `/sales`         | List sales.                                    |
| `POST`      | `/sales`         | Create a new sale with applied tax rules.      |
| `DELETE`    | `/sales/{id}`    | Cancel a sale based on its ID.                 |

- **Base URL**: `http://ocelot-gateway:7777/`

### 📦 Standardized Response Format

```json
{
  "data": [{}],
  "status": "success",
  "message": "Operation completed successfully."
}

```

## Project Structure

The project is be structured as follows:

``` 
smart-sales/
├── azure-pipelines.yml
├── docker-compose.override.yml
├── docker-compose.yml
├── jenkins.txt
├── readme.md
├── doc/
│ ├── configuration-project.md
│ ├── overview.md
├── k8s/
│ ├── db-deployment.yaml
│ ├── db-pvc.yaml
│ ├── db-service.yaml
│ ├── ocelot-deployment.yaml
│ ├── ocelot-service.yaml
│ ├── sales-api-deployment.yaml
│ └── sales-api-service.yaml
└── src/
├── Gateway/
│ ├── Dockerfile
│ ├── Gateway.csproj
│ ├── ocelot.json
│ ├── Program.cs
│ └── Properties/
│ └── launchSettings.json
├── SalesApi/
│ ├── Dockerfile
│ ├── Sales API.postman_collection.json
│ ├── SalesApi.Application/
│ │ ├── SalesApi.Application.csproj
│ │ ├── Common/
│ │ │ └── HandlerResult.cs
│ │ ├── Products/
│ │ │ ├── Commands/
│ │ │ ├── Handlers/
│ │ │ ├── Notifications/
│ │ │ ├── Profiles/
│ │ │ ├── Queries/
│ │ │ └── Validators/
│ │ └── Sales/
│ │ ├── Commands/
│ │ ├── Handlers/
│ │ ├── Notifications/
│ │ ├── Profiles/
│ │ ├── Queries/
│ │ └── Validators/
│ ├── SalesApi.Domain/
│ │ ├── SalesApi.Domain.csproj
│ │ ├── Entities/
│ │ │ ├── Product.cs
│ │ │ ├── Sale.cs
│ │ │ └── SaleItem.cs
│ │ ├── Events/
│ │ │ ├── ProductCreatedEvent.cs
│ │ │ ├── SaleCancelledEvent.cs
│ │ │ └── SaleCreatedEvent.cs
│ │ ├── Repositories/
│ │ │ ├── IProductRepository.cs
│ │ │ └── ISaleRepository.cs
│ │ └── Services/
│ │ └── Tax/
│ ├── SalesApi.Infrastructure/
│ │ ├── appsettings.json
│ │ ├── SalesApi.Infrastructure.csproj
│ │ ├── Extensions/
│ │ ├── Migrations/
│ │ ├── Persistence/
│ │ └── Repositories/
│ ├── SalesApi.Presentation/
│ │ ├── appsettings.json
│ │ ├── Program.cs
│ │ ├── SalesApi.http
│ │ ├── SalesApi.Presentation.csproj
│ │ ├── SalesApi.Presentation.csproj.user
│ │ ├── Controllers/
│ │ └── Properties/
│ ├── SalesApi.Tests/
│ │ ├── SalesApi.Tests.csproj
│ │ ├── Data/
│ │ ├── IntegrationTests/
│ │ └── UnitTests/
└── Airflow/
├── dags/
│ └── etl_sales_dag.py 
├── scripts/
│ └── etl_sales.py 
├── tests/
│ └── sales_test.py 
├── plugins
├── Dockerfile 
├── requirements.txt 
└── .env

```

