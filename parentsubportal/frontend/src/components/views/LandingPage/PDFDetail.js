import React, { Fragment } from "react";
import { Item, Label } from "semantic-ui-react";
import PostDetail from "./PostDetail";

function PDFDetail(props) {
    return (
        <PostDetail post={props.post}>
            <Label href={props.post.pdf_file}>View</Label>
        </PostDetail>
    );
}

export default PDFDetail;
