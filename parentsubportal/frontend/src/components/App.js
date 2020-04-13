import React from "react";

import { Provider } from "react-redux";
import store from "../store";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
//import Comments from "./comments/comments"
import LandingPage from "./views/LandingPage/LandingPage";
import AdminPage from "./views/admin/AdminPage";
import TopicPage from "./views/TopicPage";
import DisabilityPage from "./views/DisabilityPage";
import PDFPosts from "./views/LandingPage/PDFPosts";
import VideoPosts from "./views/LandingPage/VideoPosts";
import NavBar from "./views/NavBar";
import Search from "./SearchBar";

import { Container } from "semantic-ui-react";

import PostPage from "./views/PostPage";
import PDFPage from "./views/PDFPage";
import VideoPage from "./views/VideoPage";

function App() {
    return (
        <Provider store={store}>
            <Router>
                <Container>
                    <Search />
                    <NavBar>
                        <Switch>
                            <Route path="/adminpage" component={AdminPage} />
                            <Route path="/blogs" component={LandingPage} />
                            <Route path="/pdf" component={PDFPosts} />
                            <Route path="/video" component={VideoPosts} />
                            <Route
                                path="/topics/:topicId"
                                component={TopicPage}
                            />
                            <Route
                                exact
                                path="/posts/:postId"
                                component={PostPage}
                            />
                            <Route
                                exact
                                path="/disabilities/:disabilityId"
                                component={DisabilityPage}
                            />
                            <Route
                                exact
                                path="/pdfs/:pdfId"
                                component={PDFPage}
                            />
                            <Route
                                exact
                                path="/videos/:videoId"
                                component={VideoPage}
                            />
                        </Switch>
                    </NavBar>
                </Container>
            </Router>
        </Provider>
    );
}
ReactDOM.render(<App />, document.getElementById("app"));
