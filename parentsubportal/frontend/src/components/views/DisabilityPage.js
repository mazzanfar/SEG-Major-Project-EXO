import React, { Fragment, useEffect } from "react";
import { withRouter } from "react-router-dom";
import { Header, Item } from "semantic-ui-react";
import PostDetail from "./LandingPage/PostDetail";
import PDFDetail from "./LandingPage/PDFDetail";
import VideoDetail from "./LandingPage/VideoDetail";
import { useSelector, useDispatch } from "react-redux";
import { getTopics } from "../../actions/topics";
import { getResources } from "../../actions/resources";

function DisabilityPage(props) {
    const disabilities = useSelector(
        (state) => state.disabilities.disabilities
    );
    const resources = useSelector((state) => state.resources.resources);
    const disability = disabilities.filter(
        (disability) => disability.id == props.match.params.disabilityId
    )[0];
    const sortedResources = resources.filter((resource) =>
        resource.data.disabilities.includes(disability.id)
    );
    console.log(sortedResources);
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getTopics());
        dispatch(
            getResources({ disabilities: props.match.params.disabilityId })
        );
    }, [dispatch]);

    const getItemDetail = (resource) => {
        switch (resource.type) {
            case "pdf":
                return (
                    <Fragment>
                        <h3>PDF</h3>
                        <PDFDetail post={resource.data} />
                    </Fragment>
                );
            case "post":
                return (
                    <Fragment>
                        <h3>Post</h3>
                        <PostDetail post={resource.data} />
                    </Fragment>
                );
            case "video":
                return (
                    <Fragment>
                        <h3>Video</h3>
                        <VideoDetail post={resource.data} />
                    </Fragment>
                );
            default:
                return null;
        }
    };

    return (
        <Fragment>
            <Header>Viewing by {disability && disability.name}</Header>
            <p>{disability && disability.description}</p>
            {resources &&
                sortedResources.map((resource) => (
                    <Item.Group>{getItemDetail(resource)}</Item.Group>
                ))}
        </Fragment>
    );
}

export default withRouter(DisabilityPage);
