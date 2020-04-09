import React, { Component, Fragment } from "react";

import { Provider, useDispatch, useSelector, useEffect } from "react-redux";
import store from "../store";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
//import Comments from "./comments/comments"
import LandingPage from "./views/LandingPage/LandingPage";
import AdminPage from "./views/admin/AdminPage";
import TopicPage from "./views/TopicPage";
import PDFPosts from "./views/LandingPage/PDFPosts";
import VideoPosts from "./views/LandingPage/VideoPosts";
import NavBar from "./views/NavBar";
import Search from "./SearchBar";

import {
    Sidebar,
    Menu,
    Icon,
    Segment,
    Header,
    Image,
    Container,
} from "semantic-ui-react";

import { Link } from "react-router-dom";
import VideoDetail from "./views/LandingPage/VideoDetail";
import PostPage from "./views/PostPage";

function App() {
    return (
        <Provider store={store}>
            <Router>
                <Container>
                    <Search />
                    <NavBar>
                        <Switch>
                            <Route path="/pdfs" component={PDFPosts} />
                            <Route path="/blogs" component={LandingPage} />
                            <Route path="/videos" component={VideoPosts} />
                            <Route path="/timeline" component={LandingPage} />
                            <Route path="/adminpage" component={AdminPage} />
                            <Route
                                path="/topics/:topicId"
                                component={TopicPage}
                            />
                            <Route
                                exact
                                path="/posts/:postId"
                                component={PostPage}
                            />
                        </Switch>
                    </NavBar>
                </Container>
            </Router>
        </Provider>
    );
}
ReactDOM.render(<App />, document.getElementById("app"));
