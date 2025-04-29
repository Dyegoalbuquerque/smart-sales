# Base runtime image
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 7777

# Build stage
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /src

# Copia o csproj correto a partir do buildContext
COPY ["Gateway.csproj", "./"]

# Restaura as dependências
RUN dotnet restore "./Gateway.csproj"

# Copia o restante do código-fonte
COPY . .

# Compila o projeto
RUN dotnet build "Gateway.csproj" -c $BUILD_CONFIGURATION -o /app/build

# Publish stage
FROM build AS publish
RUN dotnet publish "Gateway.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

# Final runtime image
FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .

ENV ASPNETCORE_URLS=http://+:7777
ENTRYPOINT ["dotnet", "Gateway.dll"]
