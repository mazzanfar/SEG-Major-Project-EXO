import React from "react";
import {
    Container,
    Sidebar,
    Segment,
    Menu,
    Link,
    Icon,
    Tab,
} from "semantic-ui-react";
import PDFForm from "../Forms/PDFForm";
import VideoForm from "../Forms/VideoForm";
import TraffiChart from "./TrafficChart";
import { useDispatch } from "react-redux";
import { getUser } from "../../../actions/auth";
import { useEffect } from "react";
import { getTopics } from "../../../actions/topics";

function AdminPage() {
    const dispatch = useDispatch();
    const panes = [
        {
            menuItem: "Add PDF",
            render: () => (
                <Tab.Pane>
                    <PDFForm />
                </Tab.Pane>
            ),
        },
        {
            menuItem: "Add Video",
            render: () => (
                <Tab.Pane>
                    <VideoForm />
                </Tab.Pane>
            ),
        },
    ];

    useEffect(() => {
        dispatch(getUser(), getTopics());
    }, [dispatch]);

    return (
        <Container fluid>
            <Sidebar.Pushable as={Segment}>
                <Sidebar
                    as={Menu}
                    animation="push"
                    icon="labeled"
                    vertical
                    visible
                    width="thin"
                    color="grey"
                >
                    <Menu.Header>Hi</Menu.Header>
                    <Menu.Menu>
                        <Menu.Item as="a">Home</Menu.Item>
                        <Menu.Item as="a">Analytics</Menu.Item>
                        <Menu.Item as="a">Resources</Menu.Item>
                    </Menu.Menu>
                </Sidebar>
                <Sidebar.Pusher>
                    <Segment basic>
                        <Tab panes={panes} />
                    </Segment>
                </Sidebar.Pusher>
            </Sidebar.Pushable>
        </Container>
    );
}

export default AdminPage;
