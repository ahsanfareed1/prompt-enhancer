# Career Compass 🎯

A comprehensive AI-powered career guidance platform that helps students discover their ideal career paths through intelligent assessments, university program matching, and personalized recommendations.

## 🌟 Features

### For Students
- **AI-Powered Career Assessment**: Interactive interview system that evaluates technical skills, soft skills, and career interests
- **Personalized Career Recommendations**: Get tailored career suggestions based on your profile and assessment results
- **University Program Matching**: Find the best academic programs that align with your career goals
- **Application Management**: Track and manage university applications in one place
- **Real-time AI Chat**: Get instant guidance and answers to career-related questions

### For Administrators
- **Student Management**: Comprehensive dashboard to manage student profiles and applications
- **Career Database Management**: Add, edit, and manage career information and requirements
- **Program Management**: Manage university programs and their details
- **Analytics Dashboard**: View insights and statistics about student applications and career trends

## 🏗️ Architecture

### Backend (FastAPI + Python)
- **Framework**: FastAPI with async/await support
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT-based authentication with bcrypt password hashing
- **AI Integration**: Google Gemini AI for career recommendations and assessments
- **Vector Database**: Pinecone for semantic search and career matching
- **Web Scraping**: Selenium for university data collection

### Frontend (React + TypeScript)
- **Framework**: React 19 with TypeScript
- **Build Tool**: Vite for fast development and building
- **Styling**: Tailwind CSS for responsive design
- **Routing**: React Router for client-side navigation
- **State Management**: React Context for authentication and app state

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 12+
- Poetry (for Python dependency management)
- pnpm (for Node.js dependency management)

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Career-Compass/backend
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

   Required environment variables:
   ```env
   DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/career_compass_db
   SECRET_KEY=your-secret-key-here
   GOOGLE_API_KEY=your-gemini-api-key-here
   PINECONE_API_KEY=your-pinecone-api-key-here
   PINECONE_ENVIRONMENT=your-pinecone-environment
   ```

4. **Set up the database**
   ```bash
   # Create PostgreSQL database
   createdb career_compass_db
   
   # Run database migrations
   python create_tables.py
   ```

5. **Start the backend server**
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd ../frontend
   ```

2. **Install dependencies**
   ```bash
   pnpm install
   ```

3. **Start the development server**
   ```bash
   pnpm dev
   ```

   The frontend will be available at `http://localhost:5173`

## 📚 API Documentation

Once the backend is running, you can access:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Key API Endpoints

#### Authentication
- `POST /api/v1/auth/register` - Register a new student
- `POST /api/v1/auth/login` - Login and get JWT token

#### Students
- `GET /api/v1/students/me` - Get current student profile
- `PATCH /api/v1/students/me` - Update student profile

#### AI Services
- `POST /api/v1/ai/interview` - Start AI career assessment
- `POST /api/v1/ai/chat` - Chat with AI career advisor
- `GET /api/v1/ai/recommendations/{student_id}` - Get career recommendations

#### Programs & Careers
- `GET /api/v1/programs/` - List all university programs
- `GET /api/v1/careers/` - List all available careers
- `GET /api/v1/careers/search` - Search careers by keywords

#### Applications
- `POST /api/v1/applications/` - Submit university application
- `GET /api/v1/applications/me` - Get student's applications

## 🗄️ Database Schema

### Core Tables
- **students**: User profiles and authentication
- **careers**: Career information and requirements
- **programs**: University programs and details
- **interview_results**: AI assessment results
- **student_career_recommendations**: Personalized career suggestions
- **applications**: University application tracking

## 🤖 AI Features

### Career Assessment
- Interactive interview system using Google Gemini AI
- Evaluates technical skills, soft skills, and learning preferences
- Generates personalized career recommendations

### Vector Search
- Pinecone integration for semantic career matching
- Advanced search capabilities for finding relevant programs
- Similarity-based recommendations

### Web Scraping
- Automated university data collection
- Real-time program information updates
- Comprehensive database of academic programs

## 🛠️ Development

### Backend Development
```bash
# Run tests
poetry run pytest

# Code formatting
poetry run black .
poetry run isort .

# Database migrations
alembic upgrade head
```

### Frontend Development
```bash
# Run linting
pnpm lint

# Build for production
pnpm build

# Preview production build
pnpm preview
```

## 📁 Project Structure

```
Career-Compass/
├── backend/
│   ├── app/
│   │   ├── api/v1/          # API routes
│   │   ├── core/            # Core configuration
│   │   ├── db/              # Database models and schemas
│   │   ├── services/        # Business logic and AI services
│   │   ├── pinecone/        # Vector database setup
│   │   └── main.py          # FastAPI application
│   ├── create_tables.py     # Database initialization
│   └── pyproject.toml       # Poetry configuration
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── context/         # React context providers
│   │   ├── services/        # API service functions
│   │   ├── types/           # TypeScript type definitions
│   │   └── utils/           # Utility functions
│   ├── public/              # Static assets
│   └── package.json         # Node.js dependencies
└── README.md
```

## 🔧 Configuration

### Environment Variables

#### Backend (.env)
```env
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/career_compass_db
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30
GOOGLE_API_KEY=your-gemini-api-key-here
PINECONE_API_KEY=your-pinecone-api-key-here
PINECONE_ENVIRONMENT=your-pinecone-environment
```

#### Frontend
The frontend automatically connects to the backend API running on `http://localhost:8000`

## 🚀 Deployment

### Backend Deployment
1. Set up a PostgreSQL database
2. Configure environment variables
3. Run database migrations
4. Deploy using your preferred method (Docker, cloud services, etc.)

### Frontend Deployment
1. Build the production bundle: `pnpm build`
2. Deploy the `dist` folder to your hosting service
3. Configure API endpoints for production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the API documentation at `/docs`

## 🔮 Future Enhancements

- [ ] Mobile app development
- [ ] Advanced analytics dashboard
- [ ] Integration with more universities
- [ ] Machine learning model improvements
- [ ] Multi-language support
- [ ] Social features and networking

---

**Career Compass** - Empowering students to find their perfect career path through AI-driven insights and personalized guidance.
