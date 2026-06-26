import { NavLink } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-blue-600 text-white p-4">
      <div className="max-w-7xl mx-auto flex justify-between items-center">
        
        <h1 className="text-2xl font-bold">
          HostelMS
        </h1>

        <div className="flex gap-6">
          <NavLink to="/">Dashboard</NavLink>
          <NavLink to="/students">Students</NavLink>
          <NavLink to="/rooms">Rooms</NavLink>
          <NavLink to="/payments">Payments</NavLink>
          <NavLink to="/assign-room">Assign Room</NavLink>
        </div>

      </div>
    </nav>
  );
}

export default Navbar;