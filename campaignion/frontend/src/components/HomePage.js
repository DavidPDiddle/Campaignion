import React, { Component } from "react";
import {
  BrowserRouter as Router,
  Route,
  Link,
  Redirect,
  Routes,
} from "react-router-dom";
import Campaign from "./Campaign";
import Quest from "./Quest";
import Session from "./Session";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Routes>
          <Route path="/campaign" element={<Campaign />}></Route>
          <Route path="/quest" element={<Quest />}></Route>
          <Route path="/session" element={<Session />}></Route>
        </Routes>
      </Router>
    );
  }
}
