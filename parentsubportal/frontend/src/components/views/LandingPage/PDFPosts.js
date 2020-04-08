import React, { Fragment, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Item, Label, Modal } from "semantic-ui-react";
import PostDetail from "./PostDetail";
import { getPDFs } from "../../../actions/pdfs";
import Comments from "./Comments";

function PDFPosts() {
    const dispatch = useDispatch();
    const pdfs = useSelector((state) => state.pdfs.pdfs);

    useEffect(() => {
        dispatch(getPDFs());
    }, [dispatch]);

    return (
        <Fragment>
            <br />
            {pdfs.map((pdf) => (
                <Item.Group>
                    <PostDetail post={pdf}>
                        <br />
                        <Label href={pdf.pdf_file}>Download PDF</Label>
                    </PostDetail>
                </Item.Group>
            ))}
        </Fragment>
    );
}

export default PDFPosts;
