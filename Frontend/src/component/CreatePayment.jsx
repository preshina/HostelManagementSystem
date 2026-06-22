import { useState, useEffect } from "react";
import api from "../api/client";

function CreatePayment(){

    const [student_id,setId] = useState("");
    const [students,setStudents] = useState([]);
    const [month,setMonth] = useState("");
    const [payment,setPayment] = useState("");
    const [pay_day,setPayDay] = useState("");


    // Fetch students from API
    useEffect(() => {

    const fetchStudents = async () => {

        try {

            const response = await api.get(`/students`);

            console.log("API RESPONSE:", response.data);

            setStudents(response.data);

        } catch(error) {

            console.log("ERROR:", error);

        }

    };

    fetchStudents();

}, []);



    const handleSubmit = async (e)=>{

        e.preventDefault();

        try{

            const response = await api.post(
                `/students/${student_id}/payments`,
                {
                    payments:[
                        {
                            month: month,
                            amount_paid: Number(payment),
                            payment_date: pay_day,
                        },
                    ],
                }
            );

            console.log(response.data);

            alert(response.data.message || "Payment created");

            setId("");
            setMonth("");
            setPayment("");
            setPayDay("");

        }

        catch(error){

            console.log(error.response?.data);

            alert(JSON.stringify(error.response?.data));
        }

    };


return (

<div className="min-h-screen bg-gray-100 p-8">

<h2 className="text-3xl text-blue-600 text-center mb-8">
Create Payment
</h2>


<form onSubmit={handleSubmit}>

<div className="flex flex-col items-center gap-4">


{/* Student ID Dropdown */}

<select
className="border border-gray-300 p-2 rounded w-64"
value={student_id}
onChange={(e)=>setId(e.target.value)}
>

<option value="">
Select Student ID
</option>


{
students.map((student)=>(
    
<option 
key={student.id}
value={student.id}
>

{student.id} - {student.name}

</option>

))

}


</select>



<input
type="date"
value={month}
onChange={(e)=>setMonth(e.target.value)}
/>



<input
className="border border-gray-300 p-2 rounded w-64"
type="number"
placeholder="Payment"
value={payment}
onChange={(e)=>setPayment(e.target.value)}
/>



<input
type="date"
value={pay_day}
onChange={(e)=>setPayDay(e.target.value)}
/>


</div>


<div className="flex justify-center mt-6">

<button
type="submit"
className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
>

Create Payment

</button>

</div>


</form>


</div>

);

}

export default CreatePayment;