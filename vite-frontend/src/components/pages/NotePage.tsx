import { FC, useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

interface UserListProps {
    id: number;
    userName: string;
    // Füge hier eventuell andere benötigte Felder hinzu
}

const Navbar: FC = () => {
    const [users, setUsers] = useState<UserListProps[]>([]);
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        // API-Aufruf, um die Notizen zu holen
        axios
            .get("http://localhost:8000/api/users/")
            .then((response) => {
                setUsers(response.data);
                setLoading(false);
            })
            .catch((error) => {
                console.log("Error fetching notes: ", error);
                setError("Fehler beim Laden der Notizen.");
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <div>User Notizen...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    return (
        <nav className="w-64 h-screen bg-gray-100 p-4">
            <ul>
                {users.length > 0 ? (
                    users.map((user) => (
                        <li key={user.id}>
                            <h2 className="font-bold">{user.userName}</h2>
                            {/* Füge Links zu Notizen hinzu */}
                            <ul className="ml-4">
                                <li>
                                    <Link
                                        to={`/users/${user.id}/pages`}
                                        className="text-blue-500 hover:underline"
                                    >
                                        Alle user
                                    </Link>
                                </li>
                            </ul>
                        </li>
                    ))
                ) : (
                    <li>Keine User</li>
                )}
            </ul>
        </nav>
    );
};

export default Navbar;
