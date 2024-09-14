// Navbar.tsx
import { FC } from 'react';
import { Link } from 'react-router-dom';

const Navbar: FC = () => {
  return (
    <nav className="bg-blue-600 p-4 shadow-lg">
      <div className="container mx-auto flex justify-between items-center">
        <div className="text-white font-bold text-xl">
          <Link to="/">MyWebsite</Link>
        </div>
        <ul className="flex space-x-6">
          <li>
            <Link
              to="/"
              className="text-white hover:text-gray-200 transition duration-300"
            >
              Home
            </Link>
          </li>
          <li>
            <Link
              to="/about"
              className="text-white hover:text-gray-200 transition duration-300"
            >
              About
            </Link>
          </li>
          <li>
            <Link
              to="/contact"
              className="text-white hover:text-gray-200 transition duration-300"
            >
              Kontakt
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
