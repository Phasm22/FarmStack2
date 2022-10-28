import React from "react";
import { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import TodoView from "./componenets/TodoListView";
//npm start/

function App() {
  const [todoList, setTodoList] = useState([{}]);
  const [name, setName] = useState("");
  const [ID, setID] = useState("");
  const [dept, setDept] = useState("");
  const isInitialMount = useRef(true);

  /*
  // Read all employees
  useEffect(() => {
    axios.get("http://localhost:8000/api/todo").then((res) => {
      setTodoList(res.data);
    });
  }, []);*/

  useEffect(() => {
    if (isInitialMount.current) {
      isInitialMount.current = false;
    } else {
      // Your useEffect code here to be run on update
      axios.get("http://localhost:8000/api/todo").then((res) => {
        setTodoList(res.data);
      });
    }
  });

  // Post an Employee
  const addEmployeeHandler = () => {
    axios
      .post("http://localhost:8000/api/todo/", {
        name: name,
        id: ID,
        department: dept,
      })
      .then((res) => console.log(res));
  };

  return (
    <div className="App">
      FARMSTACK2
      <div
        className="App list-group-item justify-content-center align-items-center mx-auto"
        style={{ width: "400px", backgroundColor: "white", marginTop: "15px" }}
      >
        <h1
          className="card text-white bg-primary mb-1"
          stylename="max-width: 20rem;"
        >
          Employee Database
        </h1>
        <h6 className="card text-white bg-secondary mb-4">
          FASTAPI - React - MongoDB
        </h6>
        <div className="card-body">
          <h5 className="card text-white bg-dark mb-3"> Add an Employee</h5>
          <span className="card-text">
            <input
              className="mb-2 form-control titleIn"
              onChange={(event) => setName(event.target.value)}
              placeholder="Name Ex. Jerry Springer"
            />
            <input
              className="mb-2 form-control ID"
              onChange={(event) => setID(event.target.value)}
              placeholder="ID Number"
            />
            <input
              className="mb-2 form-control Dept"
              onChange={(event) => setDept(event.target.value)}
              placeholder="Department"
            />
            <button
              className="btn btn-outline-primary mx-2 mb-3"
              style={{ borderRadius: "50px", fontWeight: "bold" }}
              onClick={addEmployeeHandler}
            >
              Add Employee
            </button>
          </span>
          <h5 className="Card text-white bg-dark mb-3">All Employees</h5>
          <div>
            <TodoView todoList={todoList} />
          </div>
        </div>
        <h6 className="card text-dark bg-warning py-1 mb-0">
          Copyright 2022, All rights reserved &copy;
        </h6>
      </div>
    </div>
  );
}

export default App;
