import { useState } from "react";
import api from "../api/client";

function CreateRoom(){
    const[room_no, setRoomNo]=useState("");
    const[capacity,setCapacity]=useState("");
    const[price_per_std,setPrice]=useState("");
    const[status,setStatus]=useState("");

    const handleSubmit=async (e)=>{
        e.preventDefault();
        try{
            const response=await api.post("/rooms",{
                room_no,
                capacity,
                price_per_std,
                status,
            });
            alert(`Room cretaed=${response.data.room_no}`);
            setRoomNo("");
            setCapacity("");
            setPrice("");
            setStatus("");
        }catch(error){
            console.error(error);
            alert("failed to create room");
        }
    };
    return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h2 className="text-3xl text-blue-600 text-center mb-8">
        Create Room
      </h2>

      <form onSubmit={handleSubmit}>
        <div className="flex flex-col items-center gap-4">
          <input
            className="border border-gray-300 p-2 rounded w-64"
            type="text"
            placeholder="Room No"
            value={room_no}
            onChange={(e) => setRoomNo(e.target.value)}
          />

          <input
            className="border border-gray-300 p-2 rounded w-64"
            type="text"
            placeholder="capacity"
            value={capacity}
            onChange={(e) => setCapacity(e.target.value)}
          />
          <input
            className="border border-gray-300 p-2 rounded w-64"
            type="text"
            placeholder="price_per_std"
            value={price_per_std}
            onChange={(e) => setPrice(e.target.value)}
          />
          <input
            className="border border-gray-300 p-2 rounded w-64"
            type="text"
            placeholder="status"
            value={status}
            onChange={(e) => setStatus(e.target.value)}
          />
        </div>

        <div className="flex justify-center mt-6">
          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
          >
            Create Room
          </button>
        </div>
      </form>
    </div>
  );
}

export default CreateRoom;