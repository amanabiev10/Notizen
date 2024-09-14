// components/NoteDetail.tsx
import {FC, useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

interface Page {
  id: number;
  title: string;
}


const PageList: FC = () => {
  const { noteId } = useParams<{ noteId: string }>();
  const [pages, setPages] = useState<Page[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (noteId) {
      axios
        .get(`http://localhost:8000/api/notes/${noteId}/pages/`)
        .then((response) => {
          setPages(response.data);
          setLoading(false);
        })
        .catch((error) => {
          console.error('Error fetching pages:', error);
          setError('Fehler beim Laden der Seiten.');
          setLoading(false);
        });
    }
  }, [noteId]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;
  
  return (
    <div style={{ width: '12.5%' }} className=" bg-gray-200 p-4 h-screen">
      <h2 className="text-lg font-bold mb-4">Notizen</h2>
      <ul>
        {pages.map(page => (
          <li key={page.id} className="mb-2">
            <Link 
              to={`/notes/${noteId}/pages/${page.id}`}
              className="text-blue-600 hover:underline"
            >
              {page.title}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PageList;