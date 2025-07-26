import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Dashboard     from './pages/Dashboard';
import Finance_Sara from './pages/Details/Finance_Sara';

function App() {


  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard/:id" element={<Dashboard />} />
        <Route path="/dashboard/finance" element={<Finance_Sara />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App
