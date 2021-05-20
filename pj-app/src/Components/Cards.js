import React from "react";
import { Card } from "react-bootstrap";

import "../App.css";

function Cards(props) {
  return (
    <Card className="cards" style={{ width: "18rem" }}>
      <Card.Img variant="top" src={props.image} />
      <Card.Body>
        <Card.Title>{props.title}</Card.Title>
        <Card.Text>{props.text}</Card.Text>
      </Card.Body>
    </Card>
  );
}

export default Cards;
