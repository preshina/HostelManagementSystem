import { useState } from "react";
import api from "../api/client"; // wrote .. because it is outside this folder.

function AssignRoom(){
    const[student_id,setId]=useState("");
    const[room_id,setRoomId]=useState("");
    const[date,setDate]=useState("");

const handleSubmit=async (e)=>{
    e.preventDefault();  // we did preventDefault so that the page would not get reload and the data would not be refreshed before use.
    try{
        const response= await api.post(`/students/${student_id}/${room_id}/${date}/assign-room`,{
            student_id,
            room_id,
            date,

        });
        alert (`room assigned=${response.data.room_id}`);
        console.log(response.data);
        setId("");
        setRoomId("");
        setDate("");
        }catch(error){
            console.error(error);
            alert("failed to assign room");
        }
    };
    return(
        <div className="min-h-screen bg-gray-100 p-8">
      <h2 className="text-3xl text-blue-600 text-center mb-8">
        Assign Room
      </h2>
      <form onSubmit={handleSubmit}>
        <input
            className="border border-gray-300 p-2 rounded w-64"
            type="number"
            placeholder="Student Id"
            value={student_id}
            onChange={(e) => setId(e.target.value)}
          />

        <input
            className="border border-gray-300 p-2 rounded w-64"
            type="number"
            placeholder="Room Id"
            value={room_id}
            onChange={(e) => setRoomId(e.target.value)}
          />

        <input
            className="border border-gray-300 p-2 rounded w-64"
            type="date"
            placeholder="Date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
          />
          <div className="flex justify-center mt-6">
          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
          >
            Assign Room
          </button>
        </div>
      
      </form>
      </div>
    );
}
export default AssignRoom;