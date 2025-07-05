# Vehicle Rental Service

A comprehensive REST-enabled Django vehicle rental system supporting both B2C (Business-to-Consumer) and C2C (Customer-to-Customer) operations.

## Features

### Core Functionality
- **Multi-role System**: Customer, Vehicle Owner, Admin, Fleet Manager, Support Agent
- **Dual Mode Operations**: Platform-owned vehicles (B2C) and peer-to-peer rentals (C2C)
- **REST API**: Full API support for web and mobile clients
- **Authentication**: Token-based authentication with role-based access control
- **Document Verification**: KYC process with document upload and approval

### Vehicle Management
- Vehicle listing with photos and details
- Location-based search with map integration support
- Real-time availability calendar
- Vehicle approval workflow for C2C listings
- Maintenance tracking for fleet vehicles

### Booking System
- Real-time booking with time slot management
- Booking modification and cancellation
- Deposit and payment handling
- Insurance and addon services

### Payment & Financial
- Secure payment gateway integration ready
- Commission-based earnings for vehicle owners
- Automated payouts to owners
- Refund policy enforcement

### Reviews & Ratings
- Bidirectional review system
- Vehicle and user ratings
- Review-based quality control

### Dispute Resolution
- Dispute reporting with evidence upload
- Admin mediation system
- Damage accountability tracking

## Quick Start

1. **Setup Environment**:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

2. **Run Development Server**:
   ```bash
   source venv/bin/activate
   python manage.py runserver
   ```

3. **Access the System**:
   - Web Interface: http://localhost:8000/
   - API Base URL: http://localhost:8000/api/
   - Admin Panel: http://localhost:8000/admin/

## API Documentation

See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for detailed API usage.

## Technology Stack

- **Backend**: Django 5.1.5 + Django REST Framework
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Authentication**: Token-based authentication
- **File Storage**: Local storage (development) / Cloud storage ready
- **API**: RESTful API with pagination and filtering

## Project Structure

```
vehicle-rental-service/
├── vehiclerental/          # Django project settings
├── apps/                   # Modular applications
│   ├── authentication/    # User management & auth
│   ├── vehicles/          # Vehicle listings
│   ├── bookings/          # Booking system
│   ├── payments/          # Payment processing
│   ├── reviews/           # Rating system
│   └── disputes/          # Dispute resolution
├── requirements.txt        # Python dependencies
├── setup.sh               # Setup script
└── API_DOCUMENTATION.md   # API documentation
```

## Models Overview

- **User**: Extended user model with roles and verification
- **Vehicle**: Vehicle listings with location and pricing
- **Booking**: Rental bookings with time slots and payments
- **Payment**: Payment transactions and payouts
- **Review**: Bidirectional rating system
- **Dispute**: Dispute resolution system

## Security Features

- Role-based access control (RBAC)
- Document verification workflow
- Secure file upload handling
- Token-based API authentication
- Input validation and sanitization

## Scalability Considerations

- RESTful API design for microservices
- Database optimization with proper indexing
- Pagination for large datasets
- Media file handling for cloud storage
- Caching-ready architecture

## Next Steps for Production

1. Configure PostgreSQL database
2. Set up cloud storage (AWS S3/Google Cloud)
3. Implement payment gateway (Stripe/Razorpay)
4. Add real-time notifications
5. Implement GPS tracking integration
6. Set up monitoring and logging
7. Configure CI/CD pipeline
8. Add comprehensive test suite
