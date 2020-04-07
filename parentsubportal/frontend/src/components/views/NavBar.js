import React, { useState, useEffect } from "react";
import { getTopics } from "../../actions/topics";
import { Route, Switch, Link, withRouter } from "react-router-dom";
import { Sidebar, Menu, Segment } from "semantic-ui-react";
import { useSelector, useDispatch } from "react-redux";

function NavBar(props) {
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getTopics());
    }, [dispatch]);

    const topics = useSelector((state) => state.topics.topics);
    return (
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
                <Menu.Header>Topics</Menu.Header>
                <Menu.Menu>
                    {topics.map((topic) => (
                        <Menu.Item href={"/topics/" + topic.id}>
                            {topic.name}
                        </Menu.Item>
                    ))}
                </Menu.Menu>
            </Sidebar>
            <Sidebar.Pusher>
                <Segment>{props.children}</Segment>
            </Sidebar.Pusher>
        </Sidebar.Pushable>
    );
}

export default withRouter(NavBar);
