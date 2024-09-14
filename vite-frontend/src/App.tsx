import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import NoteSidebar from './components/NoteSidebar';
import PageList from './components/PageList';
import PageDetail from './components/PageDetail'; // Importiere NoteDetail

const Home: React.FC = () => <h2>Home Page</h2>;
const About: React.FC = () => <h2>About Page</h2>;
const Contact: React.FC = () => <h2>Contact Page</h2>;
const NotFound: React.FC = () => <h2>404 - Page Not Found</h2>;

const App: React.FC = () => {
  return (
    <Router>
      <Navbar /> {/* Navbar für die Navigation */}
      
      <div className="flex">
        <NoteSidebar /> {/* Sidebar mit den Notizen */}
        
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route 
            path="/notes/:noteId/*" 
            element={(
                <div className="flex w-full">
                  {/* PageList bleibt immer sichtbar */}
                  <PageList />
                  <Routes>
                    <Route path="pages/:pageId" element={<PageDetail />} />
                  </Routes>
                </div>
              )}
          />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
