import './App.css';
import background from './images/lightbkgrnd.png';
import { Carousel, Card, Button, ListGroup } from 'react-bootstrap';
import { Container, Row, Col } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import pjMain from './images/PJC1.png';
import filler from './images/imgfill.jpg';
import filler2 from './images/imgfill2.jpg';
import turtwig from './images/turtwig.png';
import piplup from './images/piplup4.png';
import chimchar from './images/chimchar4.png';






const backgroundImg = {
  width: 'fill',
  height: '150vh',
  background: 'no-repeat',
  backgroundImage: `url(${background})`,
  backgroundPosition: 'center',
  backgroundRepeat: 'no-repeat',
  backgroundSize: 'cover',
};

//create onclick function

function App() {
  return (

      <div className="App">
          <Carousel fade controls={false}>
            <Carousel.Item>

              <img
                className="d-block w-100"
                src= {pjMain}
                alt="First slide"
                style={{width:"100%", height:"100%"}}
              />
            </Carousel.Item>
            <Carousel.Item>
              <img
                className="d-block w-100"
                src={filler}
                alt="Second slide"
                style={{width:"100%", height:"100%"}}
              />

              <Carousel.Caption>
                <h3>Second slide label</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item>
              <img
                className="d-block w-100"
                src={filler2}
                alt="Third slide"
                style={{width:"100%", height:"100%"}}
              />

              <Carousel.Caption>
                <h3>Third slide label</h3>
                <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
              </Carousel.Caption>
            </Carousel.Item>
          </Carousel>









        <section style={backgroundImg}>

            <br></br>
            <Carousel interval={null}>

                    <Carousel.Item style={{ paddingLeft: '40%', paddingRight: '40%', paddingTop: '5%', paddingBottom: '5%' }}>
                      <Card style={{ width: '20rem', alignItems: 'center', background: 'rgba(0, 0, 0, 0)', border:'none' }}> 
                        <Card.Img variant="top" src={turtwig} />
                          <Card.Body>
                            <Card.Title style={{ color: 'white', fontSize: '50px' }}>Turtwig</Card.Title>
                            <ListGroup>
                              <ListGroup.Item style={{ color: 'white', backgroundColor: 'rgba(0, 0, 0, 0)', border:'none' }}><h5>Type: Grass</h5> </ListGroup.Item>
                              <ListGroup.Item style={{ color: 'white', backgroundColor: 'rgba(0, 0, 0, 0)', border:'none' }}> <h5>Ability: Overgrow</h5></ListGroup.Item>
                              <ListGroup.Item style={{ color: 'white', backgroundColor: 'rgba(0, 0, 0, 0)', border:'none' }}><h5>Role:</h5> 
                              It undertakes photosynthesis with its body, making oxygen. 
                              The leaf on its head wilts if it is thirsty. </ListGroup.Item>
                            </ListGroup>
                            <Card.Text style={{ color: 'white' }}>
                              
                              
                              

                            </Card.Text>
                            <Button variant="primary">Match Up!</Button>
                          </Card.Body>
                      </Card>
                      </Carousel.Item>

                      <Carousel.Item style={{ paddingLeft: '40%', paddingRight: '40%', paddingTop: '5%', paddingBottom: '5%' }}>
                      <Card style={{ width: '20rem', alignItems: 'center', background: 'rgba(0, 0, 0, 0)', border:'none' }}>
                        <Card.Img variant="top" src={piplup} />
                          <Card.Body>
                            <Card.Title style={{ color: 'white', fontSize: '50px' }}>Piplup</Card.Title>
                              <ListGroup>
                                <ListGroup.Item style={{ color: 'white', backgroundColor: 'rgba(0, 0, 0, 0)', border:'none' }}><h5>Type: Water</h5> </ListGroup.Item>
                                <ListGroup.Item style={{ color: 'white', backgroundColor: 'rgba(0, 0, 0, 0)', border:'none' }}> <h5>Ability: Torrent</h5></ListGroup.Item>
                                <ListGroup.Item style={{ color: 'white', backgroundColor: 'rgba(0, 0, 0, 0)', border:'none' }}><h5>Role:</h5> 
                                Its thick down guards it from cold.
                                It lives along shores in northern countries.
                                </ListGroup.Item>
                              </ListGroup>
                            <Button variant="primary">Match Up!</Button>
                          </Card.Body>
                      </Card>
                    </Carousel.Item>

                    <Carousel.Item style={{ paddingLeft: '40%', paddingRight: '40%', paddingTop: '5%', paddingBottom: '5%' }}>
                      <Card style={{ width: '20rem', alignItems: 'center', background: 'rgba(0, 0, 0, 0)', border:'none' }}> 
                        <Card.Img variant="top" src={chimchar} />
                          <Card.Body>
                            <Card.Title style={{ color: 'white', fontSize: '50px' }}>Chimchar</Card.Title>
                              <ListGroup>
                                  <ListGroup.Item style={{ color: 'white', backgroundColor: 'rgba(0, 0, 0, 0)', border:'none' }}><h5>Type: Fire</h5> </ListGroup.Item>
                                  <ListGroup.Item style={{ color: 'white', backgroundColor: 'rgba(0, 0, 0, 0)', border:'none' }}> <h5>Ability: Blaze</h5></ListGroup.Item>
                                  <ListGroup.Item style={{ color: 'white', backgroundColor: 'rgba(0, 0, 0, 0)', border:'none' }}><h5>Role:</h5> 
                                  Its fire is put out when it sleeps.
                                  Its fiery rear end is fueled by gas made in its belly. 
                                  Even rain can't extinguish the fire. </ListGroup.Item>
                                </ListGroup>
                              <Button variant="primary">Match Up!</Button>
                          </Card.Body>
                      </Card>
                      </Carousel.Item>


            </Carousel>

          <br></br>

          <div className='TeamSuggestion'>
            <h1 className="Title">TEAM SUGGESTION</h1>
          </div>


        </section>

      </div>

  );
}



export default App;
