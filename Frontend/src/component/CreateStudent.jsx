import { useState } from "react";
import api from "../api/client";

function CreateStudent() {
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await api.post("/students", {
        name,
        phone,
      });

      alert(`Student Created: ${response.data.name}`);

      setName("");
      setPhone("");
    } catch (error) {
      console.error(error);
      alert("Failed to create student");
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h2 className="text-3xl text-blue-600 text-center mb-8">
        Create Student
      </h2>

      <form onSubmit={handleSubmit}>
        <div className="flex flex-col items-center gap-4">
          <input
            className="border border-gray-300 p-2 rounded w-64"
            type="text"
            placeholder="Student Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />

          <input
            className="border border-gray-300 p-2 rounded w-64"
            type="text"
            placeholder="Phone"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
        </div>

        <div className="flex justify-center mt-6">
          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
          >
            Create Student
          </button>
        </div>
      </form>
    </div>
  );
}

export default CreateStudent;