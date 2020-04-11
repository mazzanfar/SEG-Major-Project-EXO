import React, { useState, useEffect } from "react";
import { getTopics } from "../../actions/topics";
import { getChildren } from "../../actions/children";
import { getUser } from "../../actions/auth";
import { getDisabilities } from "../../actions/disabilities";
import { Route, Switch, Link, NavLink, withRouter } from "react-router-dom";
import { Sidebar, Menu, Segment } from "semantic-ui-react";
import { useSelector, useDispatch } from "react-redux";

function NavBar(props) {
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getUser());
        dispatch(getTopics());
        // TODO: call with current user's id
        dispatch(getChildren(1));
        dispatch(getDisabilities(1));
    }, [dispatch]);

    const topics = useSelector((state) => state.topics.topics);
    const disabilities = useSelector(
        (state) => state.disabilities.disabilities
    );

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
                <Menu.Header>Resources</Menu.Header>
                <Menu.Menu>
                    <Menu.Item as={NavLink} to="/pdfs">
                        PDFs
                    </Menu.Item>
                    <Menu.Item as={NavLink} to="/videos">
                        Videos
                    </Menu.Item>
                    <Menu.Item as={NavLink} to="/blogs">
                        Blog
                    </Menu.Item>{" "}
                </Menu.Menu>
                <Menu.Header>Topics</Menu.Header>
                <Menu.Menu>
                    {topics.map((topic) => (
                        <Menu.Item as={NavLink} to={"/topics/" + topic.id}>
                            {topic.name}
                        </Menu.Item>
                    ))}
                </Menu.Menu>
                <Menu.Header>Disabilities</Menu.Header>
                <Menu.Menu>
                    {disabilities.map((disability) => (
                        <Menu.Item
                            as={NavLink}
                            to={"/disabilities/" + disability.id}
                        >
                            {disability.name}
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
