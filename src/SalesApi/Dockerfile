# Base image for runtime
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 8090

# Install PostgreSQL client (if needed)
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Build stage
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /src

# Copy project files for restore (paths relative to src/SalesApi)
COPY ["SalesApi.Presentation/SalesApi.Presentation.csproj", "SalesApi.Presentation/"]
COPY ["SalesApi.Domain/SalesApi.Domain.csproj", "SalesApi.Domain/"]
COPY ["SalesApi.Infrastructure/SalesApi.Infrastructure.csproj", "SalesApi.Infrastructure/"]
COPY ["SalesApi.Application/SalesApi.Application.csproj", "SalesApi.Application/"]

# Restore dependencies
RUN dotnet restore "SalesApi.Presentation/SalesApi.Presentation.csproj"

# Copy all source code (paths relative to src/SalesApi)
COPY SalesApi.Presentation/ SalesApi.Presentation/
COPY SalesApi.Domain/ SalesApi.Domain/
COPY SalesApi.Infrastructure/ SalesApi.Infrastructure/
COPY SalesApi.Application/ SalesApi.Application/

WORKDIR "/src/SalesApi.Presentation"
RUN dotnet build "SalesApi.Presentation.csproj" -c $BUILD_CONFIGURATION -o /app/build

# Publish stage
FROM build AS publish
RUN dotnet publish "SalesApi.Presentation.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

# Final image stage
FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .

ENV ASPNETCORE_URLS=http://+:8090

ENTRYPOINT ["dotnet", "SalesApi.Presentation.dll"]
