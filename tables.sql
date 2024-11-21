--
-- PostgreSQL database dump
--

-- Dumped from database version 16.5 (Ubuntu 16.5-1.pgdg24.04+1)
-- Dumped by pg_dump version 17.1 (Ubuntu 17.1-1.pgdg24.04+1)

-- Started on 2024-11-18 15:53:59 CET

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2 (class 3079 OID 16944)
-- Name: timescaledb; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS timescaledb WITH SCHEMA public;


--
-- TOC entry 4102 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION timescaledb; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION timescaledb IS 'Enables scalable inserts and complex queries for time-series data (Community Edition)';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 232 (class 1259 OID 16482)
-- Name: aggregated_kpi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aggregated_kpi (
    aggregated_kpi_id integer NOT NULL,
    aggregated_kpi_name text NOT NULL,
    kpi_list text NOT NULL,
    aggregated_value double precision NOT NULL,
    begin_datetime timestamp without time zone NOT NULL,
    end_datetime timestamp without time zone NOT NULL,
    asset_id character varying(50)
);


ALTER TABLE public.aggregated_kpi OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 16481)
-- Name: aggregated_kpi_aggregated_kpi_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.aggregated_kpi_aggregated_kpi_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.aggregated_kpi_aggregated_kpi_id_seq OWNER TO postgres;

--
-- TOC entry 4103 (class 0 OID 0)
-- Dependencies: 231
-- Name: aggregated_kpi_aggregated_kpi_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.aggregated_kpi_aggregated_kpi_id_seq OWNED BY public.aggregated_kpi.aggregated_kpi_id;


--
-- TOC entry 233 (class 1259 OID 16543)
-- Name: machines; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.machines (
    asset_id character varying(50) NOT NULL,
    name character varying(255) NOT NULL,
    type character varying(100) DEFAULT 'Unknown'::character varying NOT NULL,
    capacity character varying(50),
    installation_date date,
    location character varying(255),
    status character varying(50) DEFAULT 'Active'::character varying,
    description text
);


ALTER TABLE public.machines OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 16463)
-- Name: maintenance_records; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.maintenance_records (
    maintenance_id integer NOT NULL,
    start_time timestamp without time zone NOT NULL,
    end_time timestamp without time zone NOT NULL,
    responsible_operator_id integer,
    issue_description text,
    maintenance_report text,
    asset_id character varying(50)
);


ALTER TABLE public.maintenance_records OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 16462)
-- Name: maintenance_records_maintenance_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.maintenance_records_maintenance_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.maintenance_records_maintenance_id_seq OWNER TO postgres;

--
-- TOC entry 4104 (class 0 OID 0)
-- Dependencies: 229
-- Name: maintenance_records_maintenance_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.maintenance_records_maintenance_id_seq OWNED BY public.maintenance_records.maintenance_id;


--
-- TOC entry 226 (class 1259 OID 16433)
-- Name: personal_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.personal_data (
    operator_id integer NOT NULL,
    name character varying(100) NOT NULL,
    surname character varying(100) NOT NULL,
    birth_date date,
    document_id character varying(50),
    "current_role" character varying(100),
    iban character varying(34),
    residence text,
    contact_id integer
);


ALTER TABLE public.personal_data OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16432)
-- Name: personal_data_operator_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.personal_data_operator_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.personal_data_operator_id_seq OWNER TO postgres;

--
-- TOC entry 4105 (class 0 OID 0)
-- Dependencies: 225
-- Name: personal_data_operator_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.personal_data_operator_id_seq OWNED BY public.personal_data.operator_id;


--
-- TOC entry 228 (class 1259 OID 16444)
-- Name: production_logs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.production_logs (
    log_id integer NOT NULL,
    start_time timestamp without time zone NOT NULL,
    end_time timestamp without time zone NOT NULL,
    responsible_operator_id integer,
    operation_description text,
    result_summary text,
    asset_id character varying(50)
);


ALTER TABLE public.production_logs OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 16443)
-- Name: production_logs_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.production_logs_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.production_logs_log_id_seq OWNER TO postgres;

--
-- TOC entry 4106 (class 0 OID 0)
-- Dependencies: 227
-- Name: production_logs_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.production_logs_log_id_seq OWNED BY public.production_logs.log_id;


--
-- TOC entry 224 (class 1259 OID 16399)
-- Name: real_time_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.real_time_data (
    "time" timestamp without time zone NOT NULL,
    name character varying(255) NOT NULL,
    kpi character varying(100) NOT NULL,
    sum double precision,
    avg double precision,
    min double precision,
    max double precision,
    asset_id character varying(50) NOT NULL
);


ALTER TABLE public.real_time_data OWNER TO postgres;

--
-- TOC entry 3815 (class 2604 OID 17674)
-- Name: aggregated_kpi aggregated_kpi_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aggregated_kpi ALTER COLUMN aggregated_kpi_id SET DEFAULT nextval('public.aggregated_kpi_aggregated_kpi_id_seq'::regclass);


--
-- TOC entry 3814 (class 2604 OID 17675)
-- Name: maintenance_records maintenance_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintenance_records ALTER COLUMN maintenance_id SET DEFAULT nextval('public.maintenance_records_maintenance_id_seq'::regclass);


--
-- TOC entry 3812 (class 2604 OID 17676)
-- Name: personal_data operator_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.personal_data ALTER COLUMN operator_id SET DEFAULT nextval('public.personal_data_operator_id_seq'::regclass);


--
-- TOC entry 3813 (class 2604 OID 17677)
-- Name: production_logs log_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.production_logs ALTER COLUMN log_id SET DEFAULT nextval('public.production_logs_log_id_seq'::regclass);


--
-- TOC entry 3866 (class 2606 OID 16489)
-- Name: aggregated_kpi aggregated_kpi_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aggregated_kpi
    ADD CONSTRAINT aggregated_kpi_pkey PRIMARY KEY (aggregated_kpi_id);


--
-- TOC entry 3868 (class 2606 OID 16550)
-- Name: machines machines_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.machines
    ADD CONSTRAINT machines_pkey PRIMARY KEY (asset_id);


--
-- TOC entry 3864 (class 2606 OID 16470)
-- Name: maintenance_records maintenance_records_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintenance_records
    ADD CONSTRAINT maintenance_records_pkey PRIMARY KEY (maintenance_id);


--
-- TOC entry 3858 (class 2606 OID 16442)
-- Name: personal_data personal_data_document_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.personal_data
    ADD CONSTRAINT personal_data_document_id_key UNIQUE (document_id);


--
-- TOC entry 3860 (class 2606 OID 16440)
-- Name: personal_data personal_data_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.personal_data
    ADD CONSTRAINT personal_data_pkey PRIMARY KEY (operator_id);


--
-- TOC entry 3862 (class 2606 OID 16451)
-- Name: production_logs production_logs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.production_logs
    ADD CONSTRAINT production_logs_pkey PRIMARY KEY (log_id);


--
-- TOC entry 3856 (class 2606 OID 16571)
-- Name: real_time_data real_time_data_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.real_time_data
    ADD CONSTRAINT real_time_data_pkey PRIMARY KEY ("time", asset_id, kpi);


--
-- TOC entry 3939 (class 2606 OID 16572)
-- Name: aggregated_kpi aggregated_kpi_asset_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aggregated_kpi
    ADD CONSTRAINT aggregated_kpi_asset_id_fkey FOREIGN KEY (asset_id) REFERENCES public.machines(asset_id);


--
-- TOC entry 3937 (class 2606 OID 16562)
-- Name: maintenance_records maintenance_records_asset_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintenance_records
    ADD CONSTRAINT maintenance_records_asset_id_fkey FOREIGN KEY (asset_id) REFERENCES public.machines(asset_id);


--
-- TOC entry 3938 (class 2606 OID 16582)
-- Name: maintenance_records maintenance_records_responsible_operator_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintenance_records
    ADD CONSTRAINT maintenance_records_responsible_operator_fkey FOREIGN KEY (responsible_operator_id) REFERENCES public.personal_data(operator_id);


--
-- TOC entry 3935 (class 2606 OID 16557)
-- Name: production_logs production_logs_asset_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.production_logs
    ADD CONSTRAINT production_logs_asset_id_fkey FOREIGN KEY (asset_id) REFERENCES public.machines(asset_id);


--
-- TOC entry 3936 (class 2606 OID 16577)
-- Name: production_logs production_logs_responsible_operator_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.production_logs
    ADD CONSTRAINT production_logs_responsible_operator_fkey FOREIGN KEY (responsible_operator_id) REFERENCES public.personal_data(operator_id);


--
-- TOC entry 3934 (class 2606 OID 16552)
-- Name: real_time_data real_time_data_asset_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.real_time_data
    ADD CONSTRAINT real_time_data_asset_id_fkey FOREIGN KEY (asset_id) REFERENCES public.machines(asset_id);


-- Completed on 2024-11-18 15:53:59 CET

--
-- PostgreSQL database dump complete
--

