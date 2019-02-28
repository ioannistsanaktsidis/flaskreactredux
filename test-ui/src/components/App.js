import {Route, Switch } from "react-router-dom";

import {App as GApp} from "grommet";
import HomePage from "./HomePage";
import NotFoundPage from "./NotFoundPage";
import TestHeader from './Header';
import React from "react";
import { hot } from "react-hot-loader";


class App extends React.Component {
  render() {
    return (
      <GApp centered={false}>
        <TestHeader />
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route component={NotFoundPage} />
        </Switch>
      </GApp>
    );
  }
}

export default hot(module)(App);

