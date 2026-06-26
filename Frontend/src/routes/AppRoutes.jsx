import { Routes, Route } from "react-router-dom";

import Student from "../pages/Student";
import Rooms from "../pages/Rooms";
import Payments from "../pages/Payments";
import FindStudent from "../pages/FindStudent";
import Dashboard from "../pages/Dashboard";

function AppRoutes() {
  return (
    <Routes>
      <Route path="/students" element={<Student />} />
      <Route path="/rooms" element={<Rooms />} />
      <Route path="/payments" element={<Payments />} />
      <Route path="/FindStudent" element={<FindStudent />} />
      <Route path="/Dashboard" element={<Dashboard />} />
    </Routes>
  );
}

export default AppRoutes;