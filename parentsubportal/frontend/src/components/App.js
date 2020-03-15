import React, { Component, Fragment } from 'react';

import { Provider } from "react-redux";
import store from "../store";
import ReactDOM from 'react-dom'
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
//import Comments from "./comments/comments"
import LandingPage from "./views/LandingPage/LandingPage";
import Post from "./views/PostPage/Post";
import AdminPage from "./views/admin/AdminPage";

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <Router>
                    <div className="container">
                        <Switch>
                            <Route path="/blogs" component={LandingPage}/>
                            <Route path="/adminpage" component ={AdminPage}/>
                            <Route path="/test" component={LandingPage}/>
                            //<Route exact path="/post/:postId" component={Post}/>
                        </Switch>
                    </div>
                </Router>
              </Provider>
        );
    }
}
const styleLink = document.createElement("link");
styleLink.rel = "stylesheet";
styleLink.href = "https://cdn.jsdelivr.net/npm/semantic-ui/dist/semantic.min.css";
document.head.appendChild(styleLink);
ReactDOM.render(<App />, document.getElementById('app'));


