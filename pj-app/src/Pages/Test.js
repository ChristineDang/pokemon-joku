import React, { useState, useEffect } from "react";
import { Button, Table, Container, Row, Col, Jumbotron } from "react-bootstrap";
import "../App.css";
// import Cards from "../Components/Cards";
import OwlDemo from "../Components/Owl";
// const display = document.querySelector(".display--field");
//
export const Test = () => {
  const [poke, setPokemon] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetch("/pokemon")
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
      })
      .then((data) => setPokemon(data.pokemon))
      .then(setLoading(true));
  }, []);

  return (
    <>
      <Jumbotron fluid>
        <Container>
          <h1>Fluid jumbotron</h1>
          <p>
            This is a modified jumbotron that occupies the entire horizontal
            space of its parent.
          </p>
          <Button
            className="magic--button"
            id="turtwig"
            onClick={async () => {
              const main_poke =
                document.getElementsByClassName("magic--button")[0].id;
              const response = await fetch("/team", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify(main_poke), // "turtwig"
              });
              if (response.ok) {
                console.log(response.ok, main_poke);
                loading ? setLoading(false) : setLoading(true);
              } else {
                console.log("NO POST POOPOO");
              }
            }}
          >
            Click me to get data from api.py
          </Button>
        </Container>
      </Jumbotron>
      <Container>
        <Row>
          <Col>
            <OwlDemo></OwlDemo>
          </Col>
        </Row>
        <Row>
          <Col>
            <div>
              {loading ? (
                <div></div>
              ) : (
                poke.map((p) => {
                  return (
                    <Table striped bordered hover variant="dark">
                      <thead>
                        <tr>
                          <th>Name</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td key={p.name.toString()}>{p.name}</td>
                        </tr>
                      </tbody>
                    </Table>
                  );
                })
              )}
            </div>
          </Col>
        </Row>
      </Container>
    </>
  );
};
