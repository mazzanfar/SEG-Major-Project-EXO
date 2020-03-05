import React, { Component, Fragment } from 'react';
import { Admin, Resource , ListGuesser } from 'react-admin'; // eslint-disable-line import/no-unresolved
import { render } from 'react-dom';
import jsonServerProvider  from 'ra-data-json-server'


/*
const dataProvider = jsonServerProvider("https://jsonplaceholder.typicode.com/users/2");

render(
    <Admin dataProvider={dataProvider}>
        <Resource name="users" list={ListGuesser} />
    </Admin>,
    document.getElementById('app')
);
*/

import { Provider } from "react-redux";
import store from "../store";
import ReactDOM from 'react-dom'
import {HashRouter as Router, Route, Switch} from "react-router-dom";
//import Comments from "./comments/comments"
import LandingPage from "./views/LandingPage/LandingPage";
import Post from "./views/PostPage/Post";

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <Router>
                    <Fragment>
                        <div className="container">
                            <Switch>
                                <Route exact path="/" component={LandingPage}/>
                                <Route exact path="/post/:postId" component={Post}/>
                            </Switch>
                        </div>
                    </Fragment>
                </Router>
              </Provider>
        );
    }
}
ReactDOM.render(<App />, document.getElementById('app'));

