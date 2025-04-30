import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav className="bg-white shadow-lg">
      <div className="container mx-auto px-4 py-3 flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold text-primary">
          CursoPlatform
        </Link>
        <div className="flex space-x-6">
          <Link to="/" className="hover:text-primary transition">Inicio</Link>
          <Link to="/courses" className="hover:text-primary transition">Cursos</Link>
          <Link to="/news" className="hover:text-primary transition">Noticias</Link>
          <Link to="/dashboard" className="bg-primary text-white px-4 py-2 rounded-md hover:bg-primary-dark transition">
            Mi cuenta
          </Link>
        </div>
      </div>
    </nav>
  );
}