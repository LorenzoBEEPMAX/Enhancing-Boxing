import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Home from './Components/Home';  // Importa il componente della HomePage
import Navbar from './Components/DefaultComponents/Navbar'

function App() {
  return (
    <Router>
      <Navbar/>
      <Routes>
          <Route path="/" element={<Home />} />

      </Routes>
    </Router>
  );
}

export default App;
