# Class Scheduling Optimizer

## Overview

This is a Streamlit-based AI-powered class scheduling optimization system designed for higher education institutions. The application helps administrators create optimized timetables by managing complex scheduling constraints, using AI-powered optimization algorithms, maximizing resource utilization, and minimizing conflicts. The system provides a complete workflow from data input through schedule generation to visualization and analytics.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit with multi-page application structure
- **UI Pattern**: Tab-based navigation within pages for organized data entry
- **Layout**: Wide layout with responsive column-based design
- **State Management**: Streamlit session state for maintaining data across page navigation
- **Visualization**: Plotly for interactive charts and schedule visualizations

### Backend Architecture
- **Core Components**:
  - `DataManager`: Centralized data storage and validation for all scheduling entities
  - `ScheduleOptimizer`: AI-powered optimization engine using constraint satisfaction and linear programming
  - `ScheduleVisualizer`: Interactive visualization component for schedule display
  - `ScheduleExporter`: Multi-format export functionality (Excel, CSV, PDF)

### Data Management
- **Storage**: In-memory data storage using Python data structures (lists, dictionaries)
- **Data Entities**: Classrooms, batches, subjects, faculty, and scheduling constraints
- **Validation**: Real-time data validation with comprehensive error reporting
- **Session Persistence**: Data maintained across user sessions via Streamlit session state

### Optimization Engine
- **Algorithm**: Constraint satisfaction problem solving with linear programming using PuLP
- **Optimization Levels**: Three-tier system (Fast, Balanced, Thorough) for different performance requirements
- **Constraint Handling**: Multiple constraint types including time, resource, faculty, and institutional preferences
- **Time Slot Management**: Dynamic time slot generation based on institutional parameters

### Visualization System
- **Schedule Views**: Multiple visualization modes (Weekly Grid, Daily Schedule, Room Occupancy, Faculty Schedule)
- **Interactive Charts**: Plotly-based interactive visualizations with color-coded scheduling data
- **Analytics Dashboard**: Comprehensive metrics and insights with resource utilization analysis
- **Export Capabilities**: Multi-sheet Excel exports with different schedule perspectives

## External Dependencies

### Core Libraries
- **Streamlit**: Web application framework for the user interface
- **Pandas**: Data manipulation and analysis for schedule data processing
- **PuLP**: Linear programming library for optimization algorithms
- **Plotly**: Interactive visualization library for charts and schedule displays
- **NumPy**: Numerical computing support for optimization calculations
- **OpenPyXL**: Excel file generation and manipulation for export functionality

### Development Dependencies
- Python 3.x runtime environment
- Standard library modules: datetime, json, io, typing, random

### Potential Future Integrations
- Database system (PostgreSQL) for persistent data storage
- Email service integration for schedule notifications
- Calendar system integration (Google Calendar, Outlook)
- Authentication system for multi-user access
- File upload capabilities for bulk data import