#!/usr/bin/env python2.7

import process_ground_truth
import process_event_set
import process_sources
import gen_source_claim_matrix_multivar
import gen_event_size_vec


def main():
    process_ground_truth.main()
    process_event_set.main()
    process_sources.main()
    gen_source_claim_matrix_multivar.main()
    gen_event_size_vec.main()


if __name__ == '__main__':
    main()
