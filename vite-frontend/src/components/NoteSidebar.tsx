// components/Sidebar.tsx
import { FC, useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

interface Note {
  id: number;
  title: string;
}

const NoteSidebar: FC = () => {
  const [notes, setNotes] = useState<Note[]>([]);
  
  useEffect(() => {
    // Beispiel: API-Aufruf, um die Notizen zu holen
    axios.get('http://localhost:8000/api/notes')
      .then(response => {
        setNotes(response.data);
      })
      .catch(error => console.error('Error fetching notes:', error));
  }, []);

  return (
    <div style={{ width: '12.5%' }} className=" bg-gray-200 p-4 h-screen">
      <h2 className="text-lg font-bold mb-4">Notizen</h2>
      <ul>
        {notes.map(note => (
          <li key={note.id} className="mb-2">
            <Link 
              to={`/notes/${note.id}/`}
              className="text-blue-600 hover:underline"
            >
              {note.title}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NoteSidebar;
