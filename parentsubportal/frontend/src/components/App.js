import React, { Component, Fragment } from "react";

import { Provider, useDispatch } from "react-redux";
import store from "../store";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
//import Comments from "./comments/comments"
import LandingPage from "./views/LandingPage/LandingPage";
import Post from "./views/PostPage/Post";
import AdminPage from "./views/admin/AdminPage";
import TopicPage from "./views/TopicPage";
import PDFPosts from "./views/LandingPage/PDFPosts";
import VideoPosts from "./views/LandingPage/VideoPosts";

import SearchBar from "./SearchBar";

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
import TimelinePage from "./views/TopicPage";
import VideoDetail from "./views/LandingPage/VideoDetail";

function App() {
    return (
        <Provider store={store}>
            <Router>
                <Container>
                    <SearchBar />
                    <Sidebar.Pushable as={Segment}>
                        <Sidebar
                            as={Menu}
                            animation="push"
                            icon="labeled"
                            visible
                            vertical
                            width="thin"
                        >
                            <Menu.Header as={Link} to="/">
                                Resources
                            </Menu.Header>
                            <Menu.Menu>
                                <Menu.Item href="/pdfs">PDFs</Menu.Item>
                                <Menu.Item href="/videos">Videos</Menu.Item>
                            </Menu.Menu>
                            <Menu.Header as={Link} to="/blogs">
                                Blog
                            </Menu.Header>
                        </Sidebar>
                        <Sidebar.Pusher>
                            <Segment>
                                <Switch>
                                    <Route path="/pdfs" component={PDFPosts} />
                                    <Route
                                        path="/blogs"
                                        component={LandingPage}
                                    />
                                    <Route
                                        path="/videos"
                                        component={VideoPosts}
                                    />
                                    <Route
                                        path="/timeline"
                                        component={LandingPage}
                                    />
                                    <Route
                                        path="/adminpage"
                                        component={AdminPage}
                                    />
                                    <Route
                                        path="/topic/:topic"
                                        component={TopicPage}
                                    />
                                    <Route
                                        exact
                                        path="/post/:postId"
                                        component={Post}
                                    />
                                </Switch>
                            </Segment>
                        </Sidebar.Pusher>
                    </Sidebar.Pushable>
                </Container>
            </Router>
        </Provider>
    );
}
ReactDOM.render(<App />, document.getElementById("app"));
