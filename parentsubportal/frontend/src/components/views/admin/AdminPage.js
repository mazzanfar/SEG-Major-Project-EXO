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
import { withRouter } from "react-router-dom";
import TraffiChart from "./TrafficChart";
import { useDispatch, useSelector } from "react-redux";
import { getUser } from "../../../actions/auth";
import { useEffect } from "react";
import { getTopics } from "../../../actions/topics";

function AdminPage(props) {
    const user = useSelector((state) => state.auth.user);
    if (user && !user.is_staff) props.history.goBack();
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
        dispatch(getTopics());
    }, [dispatch]);

    return <Tab panes={panes} />;
}

export default withRouter(AdminPage);
