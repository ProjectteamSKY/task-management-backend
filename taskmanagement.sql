--
-- PostgreSQL database dump
--

\restrict wZHbRSgRvsfjeGO6j41Dn4QpGSEbmhhSNrxfvsdeVHH9u3OIZybYlJuPxZQIOJi

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

-- Started on 2026-05-15 11:40:49

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 244 (class 1259 OID 21734)
-- Name: projects; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.projects (
    id bigint NOT NULL,
    name text,
    description text,
    start_date date,
    end_date date,
    status character varying,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.projects OWNER TO postgres;

--
-- TOC entry 243 (class 1259 OID 21733)
-- Name: projects_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.projects_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.projects_id_seq OWNER TO postgres;

--
-- TOC entry 5199 (class 0 OID 0)
-- Dependencies: 243
-- Name: projects_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.projects_id_seq OWNED BY public.projects.id;


--
-- TOC entry 224 (class 1259 OID 21505)
-- Name: schedule_slots; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.schedule_slots (
    id bigint NOT NULL,
    worker_id bigint,
    task_id bigint,
    date date,
    start_time time without time zone,
    end_time time without time zone,
    duration_units bigint,
    status character varying
);


ALTER TABLE public.schedule_slots OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 21504)
-- Name: schedule_slots_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.schedule_slots_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.schedule_slots_id_seq OWNER TO postgres;

--
-- TOC entry 5200 (class 0 OID 0)
-- Dependencies: 223
-- Name: schedule_slots_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.schedule_slots_id_seq OWNED BY public.schedule_slots.id;


--
-- TOC entry 238 (class 1259 OID 21655)
-- Name: tags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tags (
    id bigint NOT NULL,
    name character varying NOT NULL,
    type character varying NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.tags OWNER TO postgres;

--
-- TOC entry 237 (class 1259 OID 21654)
-- Name: tags_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tags_id_seq OWNER TO postgres;

--
-- TOC entry 5201 (class 0 OID 0)
-- Dependencies: 237
-- Name: tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tags_id_seq OWNED BY public.tags.id;


--
-- TOC entry 242 (class 1259 OID 21707)
-- Name: task_assignments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.task_assignments (
    id bigint NOT NULL,
    task_id bigint,
    worker_id bigint,
    allocated_hours bigint,
    status character varying DEFAULT 'assigned'::character varying,
    start_date date NOT NULL,
    end_date date NOT NULL,
    start_time time without time zone NOT NULL,
    end_time time without time zone NOT NULL,
    duration_units integer DEFAULT 2,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.task_assignments OWNER TO postgres;

--
-- TOC entry 241 (class 1259 OID 21706)
-- Name: task_assignments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.task_assignments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.task_assignments_id_seq OWNER TO postgres;

--
-- TOC entry 5202 (class 0 OID 0)
-- Dependencies: 241
-- Name: task_assignments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.task_assignments_id_seq OWNED BY public.task_assignments.id;


--
-- TOC entry 240 (class 1259 OID 21686)
-- Name: task_dependencies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.task_dependencies (
    task_id bigint NOT NULL,
    depends_on_id bigint NOT NULL,
    CONSTRAINT task_dependencies_check CHECK ((task_id <> depends_on_id))
);


ALTER TABLE public.task_dependencies OWNER TO postgres;

--
-- TOC entry 239 (class 1259 OID 21669)
-- Name: task_tags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.task_tags (
    task_id bigint NOT NULL,
    tag_id bigint NOT NULL
);


ALTER TABLE public.task_tags OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 21479)
-- Name: tasks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tasks (
    id bigint NOT NULL,
    title character varying NOT NULL,
    description text NOT NULL,
    status character varying NOT NULL,
    priority character varying NOT NULL,
    task_type character varying DEFAULT 'GENERAL'::character varying,
    estimated_hours bigint,
    project_id bigint,
    start_date date,
    end_date date,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.tasks OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 21478)
-- Name: tasks_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tasks_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tasks_id_seq OWNER TO postgres;

--
-- TOC entry 5203 (class 0 OID 0)
-- Dependencies: 219
-- Name: tasks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tasks_id_seq OWNED BY public.tasks.id;


--
-- TOC entry 228 (class 1259 OID 21550)
-- Name: worker_availability; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.worker_availability (
    id integer NOT NULL,
    worker_id integer,
    status character varying(20) NOT NULL,
    day_of_week integer,
    start_time time without time zone,
    end_time time without time zone,
    from_date date,
    to_date date,
    leave_type character varying(50),
    reason text,
    approval_status character varying(20) DEFAULT 'pending'::character varying,
    is_enabled boolean DEFAULT true,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now()
);


ALTER TABLE public.worker_availability OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 21549)
-- Name: worker_availability_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.worker_availability_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.worker_availability_id_seq OWNER TO postgres;

--
-- TOC entry 5204 (class 0 OID 0)
-- Dependencies: 227
-- Name: worker_availability_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.worker_availability_id_seq OWNED BY public.worker_availability.id;


--
-- TOC entry 226 (class 1259 OID 21525)
-- Name: worker_capabilities; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.worker_capabilities (
    id bigint NOT NULL,
    worker_id bigint NOT NULL,
    capability character varying NOT NULL,
    proficiency integer DEFAULT 1 NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT worker_capabilities_proficiency_check CHECK (((proficiency >= 1) AND (proficiency <= 5)))
);


ALTER TABLE public.worker_capabilities OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 21524)
-- Name: worker_capabilities_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.worker_capabilities_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.worker_capabilities_id_seq OWNER TO postgres;

--
-- TOC entry 5205 (class 0 OID 0)
-- Dependencies: 225
-- Name: worker_capabilities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.worker_capabilities_id_seq OWNED BY public.worker_capabilities.id;


--
-- TOC entry 232 (class 1259 OID 21589)
-- Name: worker_emergency_contacts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.worker_emergency_contacts (
    id bigint NOT NULL,
    worker_id bigint NOT NULL,
    full_name character varying NOT NULL,
    relationship character varying,
    phone character varying NOT NULL,
    email character varying,
    address text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone
);


ALTER TABLE public.worker_emergency_contacts OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 21588)
-- Name: worker_emergency_contacts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.worker_emergency_contacts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.worker_emergency_contacts_id_seq OWNER TO postgres;

--
-- TOC entry 5206 (class 0 OID 0)
-- Dependencies: 231
-- Name: worker_emergency_contacts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.worker_emergency_contacts_id_seq OWNED BY public.worker_emergency_contacts.id;


--
-- TOC entry 234 (class 1259 OID 21611)
-- Name: worker_equipment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.worker_equipment (
    id bigint NOT NULL,
    worker_id bigint NOT NULL,
    name character varying NOT NULL,
    equipment_ref character varying NOT NULL,
    category character varying NOT NULL,
    condition character varying(10) DEFAULT 'Good'::character varying NOT NULL,
    assigned_date date NOT NULL,
    return_date date,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.worker_equipment OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 21610)
-- Name: worker_equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.worker_equipment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.worker_equipment_id_seq OWNER TO postgres;

--
-- TOC entry 5207 (class 0 OID 0)
-- Dependencies: 233
-- Name: worker_equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.worker_equipment_id_seq OWNED BY public.worker_equipment.id;


--
-- TOC entry 230 (class 1259 OID 21570)
-- Name: worker_notes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.worker_notes (
    id bigint NOT NULL,
    worker_id bigint NOT NULL,
    notes text NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone
);


ALTER TABLE public.worker_notes OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 21569)
-- Name: worker_notes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.worker_notes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.worker_notes_id_seq OWNER TO postgres;

--
-- TOC entry 5208 (class 0 OID 0)
-- Dependencies: 229
-- Name: worker_notes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.worker_notes_id_seq OWNED BY public.worker_notes.id;


--
-- TOC entry 246 (class 1259 OID 21745)
-- Name: worker_shift_schedules; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.worker_shift_schedules (
    id bigint NOT NULL,
    worker_id bigint NOT NULL,
    shift_type character varying(20) NOT NULL,
    working_days text[] DEFAULT '{}'::text[] NOT NULL,
    start_time time without time zone NOT NULL,
    end_time time without time zone NOT NULL,
    break_duration integer DEFAULT 30 NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.worker_shift_schedules OWNER TO postgres;

--
-- TOC entry 245 (class 1259 OID 21744)
-- Name: worker_shift_schedules_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.worker_shift_schedules_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.worker_shift_schedules_id_seq OWNER TO postgres;

--
-- TOC entry 5209 (class 0 OID 0)
-- Dependencies: 245
-- Name: worker_shift_schedules_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.worker_shift_schedules_id_seq OWNED BY public.worker_shift_schedules.id;


--
-- TOC entry 236 (class 1259 OID 21634)
-- Name: worker_training_development; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.worker_training_development (
    id bigint NOT NULL,
    worker_id bigint NOT NULL,
    type character varying(10) NOT NULL,
    title text NOT NULL,
    progress integer DEFAULT 0 NOT NULL,
    due_date date,
    provider character varying,
    category character varying,
    status character varying(20),
    start_date date,
    end_date date,
    notes text,
    CONSTRAINT worker_training_development_type_check CHECK (((type)::text = ANY ((ARRAY['training'::character varying, 'goal'::character varying])::text[])))
);


ALTER TABLE public.worker_training_development OWNER TO postgres;

--
-- TOC entry 235 (class 1259 OID 21633)
-- Name: worker_training_development_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.worker_training_development_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.worker_training_development_id_seq OWNER TO postgres;

--
-- TOC entry 5210 (class 0 OID 0)
-- Dependencies: 235
-- Name: worker_training_development_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.worker_training_development_id_seq OWNED BY public.worker_training_development.id;


--
-- TOC entry 222 (class 1259 OID 21495)
-- Name: workers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.workers (
    id bigint NOT NULL,
    name character varying,
    email character varying,
    role character varying,
    department character varying,
    status character varying,
    avatar character varying,
    daily_capacity_hours bigint
);


ALTER TABLE public.workers OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 21494)
-- Name: workers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.workers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.workers_id_seq OWNER TO postgres;

--
-- TOC entry 5211 (class 0 OID 0)
-- Dependencies: 221
-- Name: workers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.workers_id_seq OWNED BY public.workers.id;


--
-- TOC entry 4952 (class 2604 OID 21737)
-- Name: projects id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.projects ALTER COLUMN id SET DEFAULT nextval('public.projects_id_seq'::regclass);


--
-- TOC entry 4928 (class 2604 OID 21508)
-- Name: schedule_slots id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.schedule_slots ALTER COLUMN id SET DEFAULT nextval('public.schedule_slots_id_seq'::regclass);


--
-- TOC entry 4946 (class 2604 OID 21658)
-- Name: tags id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags ALTER COLUMN id SET DEFAULT nextval('public.tags_id_seq'::regclass);


--
-- TOC entry 4948 (class 2604 OID 21710)
-- Name: task_assignments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_assignments ALTER COLUMN id SET DEFAULT nextval('public.task_assignments_id_seq'::regclass);


--
-- TOC entry 4924 (class 2604 OID 21482)
-- Name: tasks id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tasks ALTER COLUMN id SET DEFAULT nextval('public.tasks_id_seq'::regclass);


--
-- TOC entry 4932 (class 2604 OID 21553)
-- Name: worker_availability id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_availability ALTER COLUMN id SET DEFAULT nextval('public.worker_availability_id_seq'::regclass);


--
-- TOC entry 4929 (class 2604 OID 21528)
-- Name: worker_capabilities id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_capabilities ALTER COLUMN id SET DEFAULT nextval('public.worker_capabilities_id_seq'::regclass);


--
-- TOC entry 4939 (class 2604 OID 21592)
-- Name: worker_emergency_contacts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_emergency_contacts ALTER COLUMN id SET DEFAULT nextval('public.worker_emergency_contacts_id_seq'::regclass);


--
-- TOC entry 4941 (class 2604 OID 21614)
-- Name: worker_equipment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_equipment ALTER COLUMN id SET DEFAULT nextval('public.worker_equipment_id_seq'::regclass);


--
-- TOC entry 4937 (class 2604 OID 21573)
-- Name: worker_notes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_notes ALTER COLUMN id SET DEFAULT nextval('public.worker_notes_id_seq'::regclass);


--
-- TOC entry 4954 (class 2604 OID 21748)
-- Name: worker_shift_schedules id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_shift_schedules ALTER COLUMN id SET DEFAULT nextval('public.worker_shift_schedules_id_seq'::regclass);


--
-- TOC entry 4944 (class 2604 OID 21637)
-- Name: worker_training_development id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_training_development ALTER COLUMN id SET DEFAULT nextval('public.worker_training_development_id_seq'::regclass);


--
-- TOC entry 4927 (class 2604 OID 21498)
-- Name: workers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workers ALTER COLUMN id SET DEFAULT nextval('public.workers_id_seq'::regclass);


--
-- TOC entry 5191 (class 0 OID 21734)
-- Dependencies: 244
-- Data for Name: projects; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.projects (id, name, description, start_date, end_date, status, created_at) FROM stdin;
\.


--
-- TOC entry 5171 (class 0 OID 21505)
-- Dependencies: 224
-- Data for Name: schedule_slots; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.schedule_slots (id, worker_id, task_id, date, start_time, end_time, duration_units, status) FROM stdin;
\.


--
-- TOC entry 5185 (class 0 OID 21655)
-- Dependencies: 238
-- Data for Name: tags; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tags (id, name, type, created_at) FROM stdin;
\.


--
-- TOC entry 5189 (class 0 OID 21707)
-- Dependencies: 242
-- Data for Name: task_assignments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.task_assignments (id, task_id, worker_id, allocated_hours, status, start_date, end_date, start_time, end_time, duration_units, created_at) FROM stdin;
\.


--
-- TOC entry 5187 (class 0 OID 21686)
-- Dependencies: 240
-- Data for Name: task_dependencies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.task_dependencies (task_id, depends_on_id) FROM stdin;
\.


--
-- TOC entry 5186 (class 0 OID 21669)
-- Dependencies: 239
-- Data for Name: task_tags; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.task_tags (task_id, tag_id) FROM stdin;
\.


--
-- TOC entry 5167 (class 0 OID 21479)
-- Dependencies: 220
-- Data for Name: tasks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tasks (id, title, description, status, priority, task_type, estimated_hours, project_id, start_date, end_date, created_at) FROM stdin;
\.


--
-- TOC entry 5175 (class 0 OID 21550)
-- Dependencies: 228
-- Data for Name: worker_availability; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.worker_availability (id, worker_id, status, day_of_week, start_time, end_time, from_date, to_date, leave_type, reason, approval_status, is_enabled, created_at, updated_at) FROM stdin;
\.


--
-- TOC entry 5173 (class 0 OID 21525)
-- Dependencies: 226
-- Data for Name: worker_capabilities; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.worker_capabilities (id, worker_id, capability, proficiency, created_at) FROM stdin;
\.


--
-- TOC entry 5179 (class 0 OID 21589)
-- Dependencies: 232
-- Data for Name: worker_emergency_contacts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.worker_emergency_contacts (id, worker_id, full_name, relationship, phone, email, address, created_at, updated_at) FROM stdin;
\.


--
-- TOC entry 5181 (class 0 OID 21611)
-- Dependencies: 234
-- Data for Name: worker_equipment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.worker_equipment (id, worker_id, name, equipment_ref, category, condition, assigned_date, return_date, updated_at) FROM stdin;
\.


--
-- TOC entry 5177 (class 0 OID 21570)
-- Dependencies: 230
-- Data for Name: worker_notes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.worker_notes (id, worker_id, notes, created_at, updated_at) FROM stdin;
\.


--
-- TOC entry 5193 (class 0 OID 21745)
-- Dependencies: 246
-- Data for Name: worker_shift_schedules; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.worker_shift_schedules (id, worker_id, shift_type, working_days, start_time, end_time, break_duration, updated_at) FROM stdin;
\.


--
-- TOC entry 5183 (class 0 OID 21634)
-- Dependencies: 236
-- Data for Name: worker_training_development; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.worker_training_development (id, worker_id, type, title, progress, due_date, provider, category, status, start_date, end_date, notes) FROM stdin;
\.


--
-- TOC entry 5169 (class 0 OID 21495)
-- Dependencies: 222
-- Data for Name: workers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.workers (id, name, email, role, department, status, avatar, daily_capacity_hours) FROM stdin;
\.


--
-- TOC entry 5212 (class 0 OID 0)
-- Dependencies: 243
-- Name: projects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.projects_id_seq', 1, false);


--
-- TOC entry 5213 (class 0 OID 0)
-- Dependencies: 223
-- Name: schedule_slots_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.schedule_slots_id_seq', 1, false);


--
-- TOC entry 5214 (class 0 OID 0)
-- Dependencies: 237
-- Name: tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tags_id_seq', 1, false);


--
-- TOC entry 5215 (class 0 OID 0)
-- Dependencies: 241
-- Name: task_assignments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.task_assignments_id_seq', 1, false);


--
-- TOC entry 5216 (class 0 OID 0)
-- Dependencies: 219
-- Name: tasks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tasks_id_seq', 1, false);


--
-- TOC entry 5217 (class 0 OID 0)
-- Dependencies: 227
-- Name: worker_availability_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.worker_availability_id_seq', 1, false);


--
-- TOC entry 5218 (class 0 OID 0)
-- Dependencies: 225
-- Name: worker_capabilities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.worker_capabilities_id_seq', 1, false);


--
-- TOC entry 5219 (class 0 OID 0)
-- Dependencies: 231
-- Name: worker_emergency_contacts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.worker_emergency_contacts_id_seq', 1, false);


--
-- TOC entry 5220 (class 0 OID 0)
-- Dependencies: 233
-- Name: worker_equipment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.worker_equipment_id_seq', 1, false);


--
-- TOC entry 5221 (class 0 OID 0)
-- Dependencies: 229
-- Name: worker_notes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.worker_notes_id_seq', 1, false);


--
-- TOC entry 5222 (class 0 OID 0)
-- Dependencies: 245
-- Name: worker_shift_schedules_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.worker_shift_schedules_id_seq', 1, false);


--
-- TOC entry 5223 (class 0 OID 0)
-- Dependencies: 235
-- Name: worker_training_development_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.worker_training_development_id_seq', 1, false);


--
-- TOC entry 5224 (class 0 OID 0)
-- Dependencies: 221
-- Name: workers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.workers_id_seq', 1, false);


--
-- TOC entry 4999 (class 2606 OID 21743)
-- Name: projects projects_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_pkey PRIMARY KEY (id);


--
-- TOC entry 4966 (class 2606 OID 21513)
-- Name: schedule_slots schedule_slots_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.schedule_slots
    ADD CONSTRAINT schedule_slots_pkey PRIMARY KEY (id);


--
-- TOC entry 4988 (class 2606 OID 21668)
-- Name: tags tags_name_type_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_name_type_key UNIQUE (name, type);


--
-- TOC entry 4990 (class 2606 OID 21666)
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (id);


--
-- TOC entry 4997 (class 2606 OID 21722)
-- Name: task_assignments task_assignments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_assignments
    ADD CONSTRAINT task_assignments_pkey PRIMARY KEY (id);


--
-- TOC entry 4995 (class 2606 OID 21693)
-- Name: task_dependencies task_dependencies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_dependencies
    ADD CONSTRAINT task_dependencies_pkey PRIMARY KEY (task_id, depends_on_id);


--
-- TOC entry 4992 (class 2606 OID 21675)
-- Name: task_tags task_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_tags
    ADD CONSTRAINT task_tags_pkey PRIMARY KEY (task_id, tag_id);


--
-- TOC entry 4962 (class 2606 OID 21493)
-- Name: tasks tasks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tasks
    ADD CONSTRAINT tasks_pkey PRIMARY KEY (id);


--
-- TOC entry 4974 (class 2606 OID 21563)
-- Name: worker_availability worker_availability_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_availability
    ADD CONSTRAINT worker_availability_pkey PRIMARY KEY (id);


--
-- TOC entry 4970 (class 2606 OID 21539)
-- Name: worker_capabilities worker_capabilities_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_capabilities
    ADD CONSTRAINT worker_capabilities_pkey PRIMARY KEY (id);


--
-- TOC entry 4972 (class 2606 OID 21541)
-- Name: worker_capabilities worker_capabilities_worker_id_capability_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_capabilities
    ADD CONSTRAINT worker_capabilities_worker_id_capability_key UNIQUE (worker_id, capability);


--
-- TOC entry 4980 (class 2606 OID 21601)
-- Name: worker_emergency_contacts worker_emergency_contacts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_emergency_contacts
    ADD CONSTRAINT worker_emergency_contacts_pkey PRIMARY KEY (id);


--
-- TOC entry 4982 (class 2606 OID 21603)
-- Name: worker_emergency_contacts worker_emergency_contacts_worker_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_emergency_contacts
    ADD CONSTRAINT worker_emergency_contacts_worker_id_key UNIQUE (worker_id);


--
-- TOC entry 4984 (class 2606 OID 21627)
-- Name: worker_equipment worker_equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_equipment
    ADD CONSTRAINT worker_equipment_pkey PRIMARY KEY (id);


--
-- TOC entry 4977 (class 2606 OID 21581)
-- Name: worker_notes worker_notes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_notes
    ADD CONSTRAINT worker_notes_pkey PRIMARY KEY (id);


--
-- TOC entry 5001 (class 2606 OID 21762)
-- Name: worker_shift_schedules worker_shift_schedules_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_shift_schedules
    ADD CONSTRAINT worker_shift_schedules_pkey PRIMARY KEY (id);


--
-- TOC entry 5003 (class 2606 OID 21764)
-- Name: worker_shift_schedules worker_shift_schedules_worker_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_shift_schedules
    ADD CONSTRAINT worker_shift_schedules_worker_id_key UNIQUE (worker_id);


--
-- TOC entry 4986 (class 2606 OID 21648)
-- Name: worker_training_development worker_training_development_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_training_development
    ADD CONSTRAINT worker_training_development_pkey PRIMARY KEY (id);


--
-- TOC entry 4964 (class 2606 OID 21503)
-- Name: workers workers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workers
    ADD CONSTRAINT workers_pkey PRIMARY KEY (id);


--
-- TOC entry 4993 (class 1259 OID 21704)
-- Name: idx_td_depends_on_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_td_depends_on_id ON public.task_dependencies USING btree (depends_on_id);


--
-- TOC entry 4967 (class 1259 OID 21548)
-- Name: idx_worker_capabilities_capability; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_worker_capabilities_capability ON public.worker_capabilities USING btree (capability);


--
-- TOC entry 4968 (class 1259 OID 21547)
-- Name: idx_worker_capabilities_worker_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_worker_capabilities_worker_id ON public.worker_capabilities USING btree (worker_id);


--
-- TOC entry 4978 (class 1259 OID 21609)
-- Name: idx_worker_emergency_contacts_worker_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_worker_emergency_contacts_worker_id ON public.worker_emergency_contacts USING btree (worker_id);


--
-- TOC entry 4975 (class 1259 OID 21587)
-- Name: idx_worker_notes_worker_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_worker_notes_worker_id ON public.worker_notes USING btree (worker_id);


--
-- TOC entry 5004 (class 2606 OID 21519)
-- Name: schedule_slots schedule_slots_task_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.schedule_slots
    ADD CONSTRAINT schedule_slots_task_id_fkey FOREIGN KEY (task_id) REFERENCES public.tasks(id);


--
-- TOC entry 5005 (class 2606 OID 21514)
-- Name: schedule_slots schedule_slots_worker_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.schedule_slots
    ADD CONSTRAINT schedule_slots_worker_id_fkey FOREIGN KEY (worker_id) REFERENCES public.workers(id);


--
-- TOC entry 5016 (class 2606 OID 21723)
-- Name: task_assignments task_assignments_task_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_assignments
    ADD CONSTRAINT task_assignments_task_id_fkey FOREIGN KEY (task_id) REFERENCES public.tasks(id) ON DELETE CASCADE;


--
-- TOC entry 5017 (class 2606 OID 21728)
-- Name: task_assignments task_assignments_worker_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_assignments
    ADD CONSTRAINT task_assignments_worker_id_fkey FOREIGN KEY (worker_id) REFERENCES public.workers(id) ON DELETE CASCADE;


--
-- TOC entry 5014 (class 2606 OID 21699)
-- Name: task_dependencies task_dependencies_depends_on_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_dependencies
    ADD CONSTRAINT task_dependencies_depends_on_id_fkey FOREIGN KEY (depends_on_id) REFERENCES public.tasks(id) ON DELETE CASCADE;


--
-- TOC entry 5015 (class 2606 OID 21694)
-- Name: task_dependencies task_dependencies_task_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_dependencies
    ADD CONSTRAINT task_dependencies_task_id_fkey FOREIGN KEY (task_id) REFERENCES public.tasks(id) ON DELETE CASCADE;


--
-- TOC entry 5012 (class 2606 OID 21681)
-- Name: task_tags task_tags_tag_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_tags
    ADD CONSTRAINT task_tags_tag_id_fkey FOREIGN KEY (tag_id) REFERENCES public.tags(id) ON DELETE CASCADE;


--
-- TOC entry 5013 (class 2606 OID 21676)
-- Name: task_tags task_tags_task_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.task_tags
    ADD CONSTRAINT task_tags_task_id_fkey FOREIGN KEY (task_id) REFERENCES public.tasks(id) ON DELETE CASCADE;


--
-- TOC entry 5007 (class 2606 OID 21564)
-- Name: worker_availability worker_availability_worker_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_availability
    ADD CONSTRAINT worker_availability_worker_id_fkey FOREIGN KEY (worker_id) REFERENCES public.workers(id) ON DELETE CASCADE;


--
-- TOC entry 5006 (class 2606 OID 21542)
-- Name: worker_capabilities worker_capabilities_worker_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_capabilities
    ADD CONSTRAINT worker_capabilities_worker_id_fkey FOREIGN KEY (worker_id) REFERENCES public.workers(id) ON DELETE CASCADE;


--
-- TOC entry 5009 (class 2606 OID 21604)
-- Name: worker_emergency_contacts worker_emergency_contacts_worker_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_emergency_contacts
    ADD CONSTRAINT worker_emergency_contacts_worker_id_fkey FOREIGN KEY (worker_id) REFERENCES public.workers(id) ON DELETE CASCADE;


--
-- TOC entry 5010 (class 2606 OID 21628)
-- Name: worker_equipment worker_equipment_worker_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_equipment
    ADD CONSTRAINT worker_equipment_worker_id_fkey FOREIGN KEY (worker_id) REFERENCES public.workers(id) ON DELETE CASCADE;


--
-- TOC entry 5008 (class 2606 OID 21582)
-- Name: worker_notes worker_notes_worker_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_notes
    ADD CONSTRAINT worker_notes_worker_id_fkey FOREIGN KEY (worker_id) REFERENCES public.workers(id) ON DELETE CASCADE;


--
-- TOC entry 5018 (class 2606 OID 21765)
-- Name: worker_shift_schedules worker_shift_schedules_worker_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_shift_schedules
    ADD CONSTRAINT worker_shift_schedules_worker_id_fkey FOREIGN KEY (worker_id) REFERENCES public.workers(id) ON DELETE CASCADE;


--
-- TOC entry 5011 (class 2606 OID 21649)
-- Name: worker_training_development worker_training_development_worker_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.worker_training_development
    ADD CONSTRAINT worker_training_development_worker_id_fkey FOREIGN KEY (worker_id) REFERENCES public.workers(id) ON DELETE CASCADE;


-- Completed on 2026-05-15 11:40:50

--
-- PostgreSQL database dump complete
--

\unrestrict wZHbRSgRvsfjeGO6j41Dn4QpGSEbmhhSNrxfvsdeVHH9u3OIZybYlJuPxZQIOJi

