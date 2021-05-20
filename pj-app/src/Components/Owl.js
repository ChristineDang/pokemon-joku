import React, { Component } from "react";
import OwlCarousel from "react-owl-carousel";
import "owl.carousel/dist/assets/owl.carousel.css";
import "owl.carousel/dist/assets/owl.theme.default.css";
import Cards from "../Components/Cards";
import "../App.css";

export class OwlDemo extends Component {
  render() {
    return (
      <div>
        <div className="container-fluid">
          <OwlCarousel items={3} margin={8} autoplay={true}>
            <div>
              <Cards
                image=""
                title="Testing Turtwig"
                text="Turtwig sound weird"
              />
            </div>

            <div>
              <Cards
                image=""
                title="Testing Turtwig"
                text="Turtwig sound weird"
              />
            </div>

            <div>
              <Cards
                image=""
                title="Testing Turtwig"
                text="Turtwig sound weird"
              />
            </div>
          </OwlCarousel>
        </div>
      </div>
    );
  }
}

export default OwlDemo;
