import React, { Component, useEffect } from "react";
import { connect, useDispatch, useSelector } from "react-redux";
import PropTypes from "prop-types";
import { getPDF } from "../../actions/pdfs";
import PDFDetail from "./LandingPage/PDFDetail";
import { Item } from "semantic-ui-react";

function PDFPage(props) {
    const pdfId = props.match.params.pdfId;
    const pdf = useSelector((state) => state.pdfs.pdf);
    const dispatch = useDispatch();
    console.log(pdfId);

    useEffect(() => {
        dispatch(getPDF(pdfId));
    }, [dispatch]);

    return pdf ? (
        <Item.Group>
            <PDFDetail post={pdf} />
        </Item.Group>
    ) : null;
}
export default PDFPage;
