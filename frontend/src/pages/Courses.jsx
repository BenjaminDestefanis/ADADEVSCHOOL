import { useState, useEffect } from 'react';
import CourseCard from '../components/course/CourseCard';

export default function Courses() {
  const [courses, setCourses] = useState([]);   // Estado para manejar loading y datos
  const [loading, setLoading] = useState(true);

  // Simular fetch de API
  useEffect(() => {
    const fetchCourses = async () => {
      // En un futuro esto vendrá del backend - Simulacion de Fetch API
      const mockCourses = [
        {
          id: 1,
          title: 'React Avanzado',
          description: 'Aprende React con proyectos reales',
          image: 'https://via.placeholder.com/300x200',
          duration: '20 horas',
          level: 'Intermedio',
          price: 49.99,
        },
        // Más cursos...
      ];
      
      setTimeout(() => {
        setCourses(mockCourses);
        setLoading(false);
      }, 1000);
    };

    fetchCourses();
  }, []);

  return (
    // Diseños responsive con grid de Tailwind
    <div>
      <h1 className="text-3xl font-bold mb-8">Nuestros Cursos</h1>
      
      {loading ? (
        <div className="flex justify-center">
          <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary"></div>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {courses.map(course => (
            <CourseCard key={course.id} course={course} />  /* Card - Componente reutilizable */
          ))}
        </div>
      )}
    </div>
  );
}