import { useState } from "react";
import api from "../api/client";

function Student() {
  const [studentId, setStudentId] = useState("");
  const [student, setStudent] = useState(null);

  const fetchStudent = async () => {
    try {
      const response = await api.get(`/students/${studentId}`);
      setStudent(response.data);
    } catch (error) {
      console.error(error);
      alert("Student not found");
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h2 className="text-3xl text-blue-600 text-center mb-8">
        Find Student
      </h2>

      <div className="flex justify-center gap-2 mb-8">
        <input
          className="border border-gray-300 p-2 rounded w-64"
          type="number"
          placeholder="Student ID"
          value={studentId}
          onChange={(e) => setStudentId(e.target.value)}
        />

        <button
          className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
          onClick={fetchStudent}
        >
          Search
        </button>
      </div>

      {student && (
        <div className="max-w-3xl mx-auto bg-white shadow-md rounded-lg p-6">
          <h3 className="text-2xl font-bold text-gray-800 mb-2">
            {student.name}
          </h3>

          <p className="text-gray-600 mb-1">
            <strong>Phone:</strong> {student.phone}
          </p>

          <p className="text-gray-600 mb-6">
            <strong>Room:</strong> {student.room}
          </p>

          <h4 className="text-xl font-semibold mb-4">
            Payments
          </h4>

          <table className="w-full border border-gray-300">
            <thead>
              <tr className="bg-gray-200">
                <th className="border border-gray-300 p-2">Month</th>
                <th className="border border-gray-300 p-2">
                  Amount Paid
                </th>
                <th className="border border-gray-300 p-2">
                  Status
                </th>
              </tr>
            </thead>

            <tbody>
              {student.payments.map((payment, index) => (
                <tr key={index}>
                  <td className="border border-gray-300 p-2">
                    {payment.month}
                  </td>
                  <td className="border border-gray-300 p-2">
                    {payment.amount_paid}
                  </td>
                  <td className="border border-gray-300 p-2">
                    {payment.status}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Student;