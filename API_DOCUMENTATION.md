# Vehicle Rental System API Documentation

## Overview
This is a REST-enabled Django vehicle rental system supporting both B2C and C2C operations with web and mobile client support.

## Authentication
All API endpoints (except registration and login) require token authentication.
Include the token in the Authorization header: `Authorization: Token <your_token>`

## API Endpoints

### Authentication Module
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `GET/PUT /api/auth/profile/` - User profile management

### Vehicles Module
- `GET /api/vehicles/` - List available vehicles (with filtering)
- `POST /api/vehicles/` - Create new vehicle listing
- `GET /api/vehicles/{id}/` - Get vehicle details
- `PUT /api/vehicles/{id}/` - Update vehicle
- `DELETE /api/vehicles/{id}/` - Delete vehicle
- `GET /api/vehicles/my-vehicles/` - List user's owned vehicles

### Bookings Module
- `GET /api/bookings/` - List user's bookings
- `POST /api/bookings/` - Create new booking
- `GET /api/bookings/{id}/` - Get booking details
- `PUT /api/bookings/{id}/` - Update booking
- `GET /api/bookings/owner-bookings/` - List bookings for owned vehicles

### Payments Module
- `GET /api/payments/` - List user's payments

### Reviews Module
- `GET /api/reviews/` - List user's reviews
- `POST /api/reviews/` - Create new review

### Disputes Module
- `GET /api/disputes/` - List user's disputes
- `POST /api/disputes/` - Create new dispute

## Query Parameters

### Vehicle Filtering
- `type` - Filter by vehicle type (car, bike, truck, van)
- `owner_type` - Filter by owner type (platform, peer)
- `location` - Filter by location (partial match)

## User Roles
- `customer` - Can rent vehicles
- `owner` - Can list vehicles for rent
- `admin` - Full system access
- `fleet_manager` - Manage platform vehicles
- `support` - Handle disputes and support

## Sample Requests

### Register User
```json
POST /api/auth/register/
{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secure_password",
    "phone": "+1234567890",
    "role": "customer"
}
```

### Create Vehicle Listing
```json
POST /api/vehicles/
{
    "title": "Honda Civic 2020",
    "description": "Well-maintained sedan",
    "vehicle_type": "car",
    "owner_type": "peer",
    "price_per_hour": 25.00,
    "location": "New York",
    "registration_number": "ABC123",
    "manufactured_date": "2020-01-01"
}
```

### Create Booking
```json
POST /api/bookings/
{
    "vehicle": 1,
    "start_time": "2024-01-15T10:00:00Z",
    "end_time": "2024-01-15T18:00:00Z",
    "total_amount": 200.00,
    "deposit_amount": 50.00
}
```