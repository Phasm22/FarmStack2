import axios from "axios";
import React from "react";

function TodoItem(props) {
  const deleteEmpHandler = (name) => {
    axios
      .delete(`http://localhost:8000/api/todo/${name}`)
      .then((res) => console.log(res.data));
    return (
      <div>
        <p>
          <span style={{ fontWeight: "bold, underline" }}>
            {props.todo.name} :
          </span>
          {props.todo.dept}
          <button
            onClick={() => deleteEmpHandler(props.todo.name)}
            className="btn btn-outline-danger my-2 mx-2"
            style={{ borderRadius: "50px" }}
          >
            X
          </button>
          <hr></hr>
        </p>
      </div>
    );
  };
}

export default TodoItem;
