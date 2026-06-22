import CreateStudent from "./component/CreateStudent";
import Student from "./component/Student";
import CreateRoom from "./component/CreateRoom";
import CreatePayment from "./component/CreatePayment";

import AssignRoom from "./component/AssignRoom";
function App() {
  return (
    <div className="bg-gray-100 p-8">
      <h1 className="text-3xl font-bold text-blue-600 flex justify-center">
        Hostel Management System
      </h1>

      <CreateStudent />
          
      <CreateRoom />

      <CreatePayment />

      <AssignRoom />

      <Student />
    </div>
  );
}

export default App;