// components/NoteDetail.tsx
import { FC, useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

interface Page {
  id: number;
  title: string;
  content: string;
  created_at: string;
  updated_at: string;
}

const PageDetail: FC = () => {
  const { noteId, pageId } = useParams<{ noteId: string, pageId: string }>();
  const [page, setPage] = useState<Page | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (noteId && pageId) {
      axios
        .get(`http://localhost:8000/api/notes/${noteId}/pages/${pageId}`)
        .then((response) => {
          setPage(response.data);
          setLoading(false);
        })
        .catch((error) => {
          console.error('Error fetching pages:', error);
          setError('Fehler beim Laden der Seiten.');
          setLoading(false);
        });
    }
  }, [noteId, pageId]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;

  if (!page) return <p>Keine Seite gefunden.</p>;

  return (
    <div style={{ width: '75%' }} className="p-6">
      <div className="bg-white p-4 rounded shadow">
        <h1 className="text-2xl font-bold mb-4">{page.title}</h1>
        <p>{page.content}</p>
        <small className="block text-gray-500 mt-4">
          Erstellt am: {new Date(page.created_at).toLocaleDateString()}
        </small>
        <small className="block text-gray-500">
          Aktualisiert am: {new Date(page.updated_at).toLocaleDateString()}
        </small>
      </div>
    </div>
  );
};

export default PageDetail;
